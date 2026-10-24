"""Exercise the real YAML automations with a virtual clock and component states.

Run with: python -m unittest discover -s tests -v (requires PyYAML).
This checks scheduling and cancellation, not audio inference or ESP32 hardware.
"""

import heapq
from pathlib import Path
import re
import unittest

import yaml


class FirmwareLoader(yaml.SafeLoader):
    pass


FirmwareLoader.add_constructor("!lambda", lambda loader, node: loader.construct_scalar(node))
CONFIG = yaml.load(
    (Path(__file__).resolve().parents[1] / "ultimatesensor-mini-v1/voice-assistant.yaml").read_text(),
    Loader=FirmwareLoader,
)


class AutomationClock:
    """Small interpreter for the ESPHome actions used by these scenarios.

    Component events are supplied by tests, independently of firmware delays.
    Unknown actions/conditions fail instead of silently masking a regression.
    """

    def __init__(self):
        self.now = 0
        self.queue = []
        self.sequence = 0
        self.scripts = {}
        self.wake_enabled = True
        self.voice_running = False
        self.playing = False
        self.announcing = False
        self.wake_running = False
        self.stop_latency = 80
        self.starts = 0
        self.phase = "replying"

    def condition(self, condition):
        if isinstance(condition, list):
            return all(self.condition(item) for item in condition)
        key, value = next(iter(condition.items()))
        if key == "and":
            return all(self.condition(item) for item in value)
        if key == "or":
            return any(self.condition(item) for item in value)
        if key == "not":
            return not self.condition(value)
        return {
            "switch.is_on": lambda: self.wake_enabled,
            "switch.is_off": lambda: not self.wake_enabled,
            "voice_assistant.is_running": lambda: self.voice_running,
            "micro_wake_word.is_running": lambda: self.wake_running,
            "media_player.is_playing": lambda: self.playing,
            "media_player.is_announcing": lambda: self.announcing,
            "media_player.is_idle": lambda: not self.playing and not self.announcing,
        }[key]()

    def enqueue(self, delay, callback):
        self.sequence += 1
        heapq.heappush(self.queue, (self.now + delay, self.sequence, callback))

    def fire(self, actions, script=None):
        if script in self.scripts:
            self.scripts[script][0] = False
        active = [True]
        if script:
            self.scripts[script] = active
        iterator = self.actions(actions)

        def resume():
            if active[0]:
                try:
                    self.enqueue(next(iterator), resume)
                except StopIteration:
                    active[0] = False

        resume()

    def actions(self, actions):
        for action in actions:
            key, value = next(iter(action.items()))
            if key == "if":
                branch = "then" if self.condition(value["condition"]) else "else"
                yield from self.actions(value.get(branch, []))
            elif key == "delay":
                match = re.fullmatch(r"(\d+)(ms|s)", str(value))
                yield int(match[1]) * (1 if match[2] == "ms" else 1000)
            elif key == "wait_until":
                condition = value.get("condition", value)
                while not self.condition(condition):
                    yield 10
            elif key == "script.execute":
                definition = next(item for item in CONFIG["script"] if item["id"] == value)
                if value != "reset_voice_led":
                    self.fire(definition["then"], script=value)
            elif key == "script.stop":
                if value in self.scripts:
                    self.scripts[value][0] = False
            elif key == "micro_wake_word.stop":
                if self.wake_running:
                    self.enqueue(self.stop_latency, lambda: setattr(self, "wake_running", False))
            elif key == "micro_wake_word.start":
                if self.wake_running:
                    continue  # ESPHome rejects start while still stopping/running.
                if self.voice_running or self.playing or self.announcing:
                    raise AssertionError("Wake word started before the response finished")
                self.wake_running = True
                self.starts += 1
            elif key == "lambda":
                phase = re.search(r"id\(voice_assistant_phase\) = \$\{voice_assist_(\w+)_phase_id\}", value)
                if phase:
                    self.phase = phase[1]
            elif key == "voice_assistant.stop":
                self.voice_running = False
            elif key == "voice_assistant.start":
                if self.wake_running:
                    raise AssertionError("Assist started before wake-word detection stopped")
                self.voice_running = True
            elif key not in ("logger.log", "light.turn_on", "light.turn_off"):
                raise AssertionError(f"Unsupported test action: {key}")

    def advance(self, milliseconds):
        end = self.now + milliseconds
        while self.queue and self.queue[0][0] <= end:
            self.now, _, callback = heapq.heappop(self.queue)
            callback()
        self.now = end

    def finish_pipeline(self):
        self.fire(CONFIG["voice_assistant"]["on_end"])

    def mute(self):
        self.wake_enabled = False
        self.fire(CONFIG["switch"][0]["turn_off_action"])


class WakeWordRecoveryTest(unittest.TestCase):
    def test_microphone_handoff_waits_for_slow_wake_word_shutdown(self):
        clock = AutomationClock()
        clock.wake_running = True
        clock.stop_latency = 1500
        clock.fire(CONFIG["micro_wake_word"]["on_wake_word_detected"])
        clock.advance(1000)
        self.assertFalse(clock.voice_running)
        clock.advance(1000)
        self.assertTrue(clock.voice_running)
        self.assertFalse(clock.wake_running)

    def test_mute_cancels_pending_microphone_handoff(self):
        clock = AutomationClock()
        clock.wake_running = True
        clock.stop_latency = 1500
        clock.fire(CONFIG["micro_wake_word"]["on_wake_word_detected"])
        clock.advance(100)
        clock.mute()
        clock.advance(2000)
        self.assertFalse(clock.voice_running)
        self.assertFalse(clock.wake_running)
        self.assertEqual(clock.phase, "muted")

    def test_repeated_commands_wait_for_long_response(self):
        clock = AutomationClock()
        for duration in (4000, 20000, 70000, 1000):
            clock.wake_running = False  # Detection stops the local listener.
            clock.voice_running = clock.playing = True
            clock.phase = "replying"
            previous = clock.starts
            clock.finish_pipeline()  # HA run-end arrives before playback ends.
            clock.advance(duration)
            self.assertFalse(clock.wake_running)
            clock.voice_running = clock.playing = False
            clock.advance(1000)
            self.assertTrue(clock.wake_running)
            self.assertEqual(clock.starts, previous + 1)
            self.assertEqual(clock.phase, "idle")

    def test_repeated_stt_errors_restore_wake_word(self):
        clock = AutomationClock()
        for _ in range(5):
            clock.wake_running = False
            clock.voice_running = True
            clock.fire(CONFIG["voice_assistant"]["on_error"])
            clock.advance(500)
            self.assertFalse(clock.wake_running)
            clock.voice_running = False
            clock.advance(1500)
            self.assertTrue(clock.wake_running)
            self.assertEqual(clock.phase, "idle")

    def test_end_and_error_events_do_not_start_two_listeners(self):
        clock = AutomationClock()
        clock.voice_running = True
        clock.fire(CONFIG["voice_assistant"]["on_error"])
        clock.finish_pipeline()
        clock.advance(500)
        self.assertEqual(clock.starts, 0)
        clock.voice_running = False
        clock.advance(2000)
        self.assertTrue(clock.wake_running)
        self.assertEqual(clock.phase, "idle")

    def test_response_without_audio_recovers(self):
        clock = AutomationClock()
        clock.finish_pipeline()
        clock.advance(1000)
        self.assertTrue(clock.wake_running)

    def test_phase_stays_replying_until_listening_resumes(self):
        clock = AutomationClock()
        clock.voice_running = clock.playing = True
        clock.finish_pipeline()
        clock.advance(5000)
        self.assertEqual(clock.phase, "replying")
        clock.voice_running = clock.playing = False
        clock.advance(1000)
        self.assertEqual(clock.phase, "idle")

    def test_announcement_blocks_restart_even_when_voice_is_idle(self):
        clock = AutomationClock()
        clock.announcing = True
        clock.finish_pipeline()
        clock.advance(3000)
        self.assertFalse(clock.wake_running)
        clock.announcing = False
        clock.advance(1000)
        self.assertTrue(clock.wake_running)

    def test_mute_cancels_pending_response_recovery(self):
        clock = AutomationClock()
        clock.voice_running = clock.playing = True
        clock.finish_pipeline()
        clock.advance(1000)
        clock.mute()
        clock.voice_running = clock.playing = False
        clock.advance(5000)
        self.assertFalse(clock.wake_running)
        self.assertEqual(clock.phase, "muted")

    def test_mute_during_listener_stop_does_not_restart(self):
        clock = AutomationClock()
        clock.wake_running = True
        clock.stop_latency = 1500
        clock.finish_pipeline()
        clock.advance(100)
        clock.mute()
        clock.advance(2000)
        self.assertFalse(clock.wake_running)

    def test_slow_listener_shutdown_is_awaited(self):
        clock = AutomationClock()
        clock.wake_running = True
        clock.stop_latency = 1500
        clock.finish_pipeline()
        clock.advance(3000)
        self.assertTrue(clock.wake_running)
        self.assertEqual(clock.starts, 1)

    def test_disconnect_cancels_pending_restart(self):
        clock = AutomationClock()
        clock.voice_running = clock.playing = True
        clock.finish_pipeline()
        clock.advance(1000)
        clock.fire(CONFIG["voice_assistant"]["on_client_disconnected"])
        clock.playing = False
        clock.advance(3000)
        self.assertFalse(clock.wake_running)
        self.assertEqual(clock.phase, "not_ready")
        clock.fire(CONFIG["voice_assistant"]["on_client_connected"])
        clock.advance(1000)
        self.assertTrue(clock.wake_running)


if __name__ == "__main__":
    unittest.main()
