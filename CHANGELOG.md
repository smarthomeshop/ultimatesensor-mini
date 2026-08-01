# Changelog

All notable customer-facing firmware changes for UltimateSensor Mini are tracked in this file.

This changelog starts on 2026-04-21. Earlier firmware versions existed before that date, but they were not tracked in a customer-facing changelog.

## [Unreleased]

- Added explicit wall-mounting and radar-model metadata for Room Designer to
  Mini V1 LD2450 and every Mini V2 LD2450/LD2460 firmware variant.
- Mini V1 beta now uses the same production LD2450 component, polygon zones,
  entry lines, people counting and stale-target handling as regular Mini V1.
- Removed the duplicated legacy LD2450 and SPS30 implementation from the Mini
  V1 beta compatibility builds.

## [UltimateSensor Mini Beta V1 2.40-beta.94] - 2026-07-31


- Mini V2 LD2460 upgrade firmware now includes the shared polygon zones,
  exclusion zones, entry lines and people-counting package used by
  UltimateSensor V2.
- Mini V2 now includes optional automatic LED lighting: a white motion light,
  warm scheduled night light, and orange/red CO2 warning flashes. All
  automatic lighting features default to off and retain their settings after
  a restart.
- Mini V2 SmartHomeShop App firmware now supports cloud configuration and
  acknowledgement for the same LED lighting settings.
- Fixed Mini V2 Thread firmware defining the LD2412 UART twice, so Thread
  variants use the same valid radar bus package as WiFi and Ethernet.
- Fixed LD2450 target coordinates retaining an old value after a target leaves;
  unavailable target updates now bypass throttling in Mini V1 beta and Mini V2.


## [UltimateSensor Mini V2 1.11] - 2026-07-31


- Mini V2 LD2460 upgrade firmware now includes the shared polygon zones,
  exclusion zones, entry lines and people-counting package used by
  UltimateSensor V2.
- Mini V2 now includes optional automatic LED lighting: a white motion light,
  warm scheduled night light, and orange/red CO2 warning flashes. All
  automatic lighting features default to off and retain their settings after
  a restart.
- Mini V2 SmartHomeShop App firmware now supports cloud configuration and
  acknowledgement for the same LED lighting settings.
- Fixed Mini V2 Thread firmware defining the LD2412 UART twice, so Thread
  variants use the same valid radar bus package as WiFi and Ethernet.
- Fixed LD2450 target coordinates retaining an old value after a target leaves;
  unavailable target updates now bypass throttling in Mini V1 beta and Mini V2.


## [UltimateSensor Mini V1 3.4] - 2026-07-31


### UltimateSensor Mini V1

- Fixed adopted ESPHome Dashboard configurations failing to compile because
  `audio/boot1.mp3` was not present next to the customer's YAML file. The boot
  sound is now downloaded from the product repository while compiling and
  remains embedded in the firmware for fully local playback.


## [UltimateSensor Mini Beta V1 2.39-beta.93] - 2026-07-31


### UltimateSensor Mini V1

- Fixed adopted ESPHome Dashboard configurations failing to compile because
  `audio/boot1.mp3` was not present next to the customer's YAML file. The boot
  sound is now downloaded from the product repository while compiling and
  remains embedded in the firmware for fully local playback.


## [UltimateSensor Mini V2 1.10] - 2026-07-30


### UltimateSensor Mini V2

- Calibration, tracking and other persisted settings are now written to flash
  within 10 seconds instead of the default one-minute delay, reducing the
  chance of recently changed settings being lost during a power interruption.


## [UltimateSensor Mini V1 3.3] - 2026-07-30


- Fixed Mini V1 temperature offset reverting to its default after every reboot
  or power cycle.
- Calibration, tracking and other persisted settings are now written to flash
  within 10 seconds instead of the default one-minute delay, reducing the
  chance of recently changed settings being lost during a power interruption.


## [UltimateSensor Mini V1 3.2] - 2026-07-28


- Fixed the remaining Mini V1 Voice Assistant issue where Assist returned to
  idle after one command but on-device wake-word detection did not reliably
  start again.
- Wake-word detection now waits for the Voice Assistant, announcement and I2S
  speaker pipelines to be fully idle instead of relying on a fixed 300 ms
  delay.
- Removed the redundant manual Micro Wake Word stop during detection, added an
  idle-state retry and expanded the recovery watchdog to also recover when
  Voice Assistant is idle but wake-word detection is not running.


## [UltimateSensor Mini V1 3.1] - 2026-07-28


- Fixed Voice Assistant sometimes remaining in Speech output after the first
  command, leaving the green LED on and preventing the local wake word from
  being detected again.
- Removed the unbounded media-player wait from the Voice Assistant completion
  path and now restart wake-word detection after both successful and failed
  voice requests.
- Added a 60-second recovery watchdog that stops a stalled voice/audio pipeline
  and restores local wake-word detection automatically.


## [UltimateSensor Mini V1 3.0] - 2026-07-27


- UltimateSensor Mini V1 production now uses the former beta runtime: ESP-IDF,
  on-device wake-word recognition, embedded boot audio and the shared native
  LD2450 tracking platform with polygon zones, exclusions, entry lines and
  people counting.
- The V1 production identity, Basic/Complete variants, local/SmartHomeShop App
  variants, firmware selector and production manifests remain available.
- Existing V1 installations on version 2.42 or older must install this
  framework migration once over USB-C at `smarthomeshop.io/firmware`. Normal
  OTA updates resume after the USB-C installation.
- The separate V1 beta track is superseded by this production release. Beta
  users should select a normal V1 production variant during the USB-C
  installation.
- V1 cloud telemetry now reports the new polygon-zone target counts.


## [UltimateSensor Mini Beta V1 2.38-beta.86] - 2026-07-25



- The UltimateSensor Mini beta now pulses the front light while the start-up sound plays, so you can see as well as hear that the sensor is booting.

- Restored the start-up sound on the UltimateSensor Mini beta firmware, so the sensor confirms out loud that it has booted. The sound can be turned off per device with the new Boot Sound switch.


## [UltimateSensor Mini V2 1.9] - 2026-07-24


- V2: Corrected the default SCD41 temperature self-heating compensation from `13.2` to `10.2` °C for all WiFi, Ethernet, Basic, Complete, cloud and LD2460 firmware variants.


## [UltimateSensor Mini V1 2.42] - 2026-07-23


### UltimateSensor Mini V1

- Rebuilt the V1 local and SmartHomeShop App cloud firmware variants with the current shared cloud configuration.
- Cloud-only firmware no longer reboots every 15 minutes when Home Assistant is not connected.
- The V1 firmware remains WiFi-only and keeps its existing microphone, speaker, media player, LD2450 tracking and optional SPS30 variant behaviour.


## [UltimateSensor Mini V2 1.8] - 2026-07-23


### UltimateSensor Mini V2

- Rebuilt all V2 firmware families: WiFi, Ethernet, Basic, Complete, SmartHomeShop App cloud, standard LD2450 and optional LD2460 upgrade variants.
- Added the final hardware UART mappings: LD2412 remains on GPIO21/GPIO20; LD2450 uses GPIO18/GPIO19; LD2460 upgrade firmware uses GPIO4/GPIO5.
- Standard V2 hardware continues to use LD2412 plus LD2450. LD2460 firmware is only for devices where LD2450 has physically been replaced, while LD2412 remains installed.
- Moved V2 tracking integration to the shared SmartHomeShop LD2450 and LD2460 packages so tracking, zones and upgrade behaviour stay consistent across firmware variants.
- Added the SmartHomeShop branded setup portal to all V2 WiFi variants, including WiFi onboarding, Home Assistant and cloud choices, and the firmware selector for WiFi/Ethernet and Basic/Complete variants.
- Kept the ESPHome captive portal and BLE Improv provisioning available. Serial Improv remains disabled on V2 because both ESP32-C6 hardware UARTs are reserved for the radar modules.
- Added V2 web-server sorting groups for Air Quality and Presence, including SPS30 measurements in Complete firmware.
- Added CPU temperature to the cloud telemetry payload and corrected V2 cloud zone count IDs for the shared tracking package.
- Fixed the V2 LD2450 integration wrapper so it uses the shared package's `tracking_radar` and `tracking_presence` IDs without redefining them, allowing all V2 LD2450 WiFi, Ethernet and cloud builds to compile.
- Removed the duplicate local LD2450 UART declaration so the shared package owns GPIO18/GPIO19 exactly once across every standard LD2450 variant.
- Published the complete V2 firmware matrix and manifests atomically, so WiFi, Ethernet, LD2450 and LD2460 variants are released together.
- The production pipeline publishes V1 and V2 firmware separately from the optional beta track.
- V2 production builds retain LD2412 on the dedicated UART while the shared tracking package owns the LD2450/LD2460 UART.


## [UltimateSensor Mini V2 1.7] - 2026-07-10

- Removed compile-time placeholder WiFi credentials from UltimateSensor Mini V2 WiFi firmware so website-flashed devices no longer try to connect to a placeholder WiFi network.
- Changed the UltimateSensor Mini V2 fallback hotspot password to `ultimatesensor-mini-v2`, matching the fallback hotspot SSID.
- Added a Firmware Variant selector and firmware update entity to all UltimateSensor Mini V2 configurations, matching the existing V1 selector. Switching between WiFi/Ethernet, Basic/Complete and local/cloud variants now points the built-in updater at the right firmware, and it automatically stays on the LD2450 or LD2460 tracking family that matches the installed hardware.
- Added local/Home Assistant Thread firmware variants for UltimateSensor Mini V2 installations that join an existing Thread network through a border router.
- Changed cloud firmware status LED behaviour so cloud-only devices blink while offline or not set up, then turn the status LED off once online instead of blinking because Home Assistant API is not connected.

## [UltimateSensor Mini V1 2.41] - 2026-07-10

- Changed cloud firmware status LED behaviour so cloud-only devices blink while offline or not set up, then turn the status LED off once online instead of blinking because Home Assistant API is not connected.

## [UltimateSensor Mini V2 1.6] - 2026-07-07


- Fixed UltimateSensor Mini V2 temperature and humidity readings: the SCD41 self-heating offset was accidentally applied twice with opposite signs, so devices reported the raw self-heated temperature (roughly 9-13 °C too high) and an over-corrected, far too high humidity. This also skewed the VOC/NOx compensation inputs.
- Added "Temperature Offset" and "Humidity Offset" controls to UltimateSensor Mini V2 in Home Assistant for per-device fine-tuning on top of the built-in self-heating compensation.


## [UltimateSensor Mini V1 2.40] - 2026-07-07


- Renamed the UltimateSensor Mini V1 "Boot sound" switch to "Boot sound & animation": turning it off now also skips the white boot LED animation on the front and back lights, so the device boots completely silent and dark.


## [UltimateSensor Mini V1 2.39] - 2026-07-07


- Fixed UltimateSensor Mini V1 boot sound playback by embedding the sound in the firmware instead of streaming it from smarthomeshop.io at boot. On networks that block that download, the firmware endlessly retried the URL, flooding the logs with "Failed to open URL" errors and keeping the red status LED flashing (#37).
- Added a "Boot sound" switch to UltimateSensor Mini V1 so the boot sound can be turned off from Home Assistant without reflashing.


## [UltimateSensor Mini Beta V1 2.37-beta.62] - 2026-07-04


- Fixed UltimateSensor Mini V1 beta temperature and humidity readings showing long unrounded decimals after applying the calibration offset.


## [UltimateSensor Mini Beta V1 2.36-beta.61] - 2026-07-04


- Added polygon detection zones, exclusion zones and entry lines with people counting to the UltimateSensor Mini V1 beta firmware via the shared smarthomeshop/ld2450 packages, including the SmartHomeShop panel push API.
- Added per-target X/Y coordinate sensors to the UltimateSensor Mini V1 beta firmware for live target tracking in the SmartHomeShop panel.


## [UltimateSensor Mini V1 2.38] - 2026-07-02


- Fixed UltimateSensor Mini V1 boot audio so local cloud tests can disable the boot sound and firmware skips the boot sound when WiFi is not connected.


## [UltimateSensor Mini V2 1.5] - 2026-06-27


- Changed the UltimateSensor Mini V2 WiFi onboarding hotspot password to match the V1 onboarding password.


## [UltimateSensor Mini V2 1.4] - 2026-06-04


- Added BLE Improv provisioning to UltimateSensor Mini V2 WiFi firmware variants for Made for ESPHome WiFi onboarding without reserving a serial UART.


## [UltimateSensor Mini V2 1.3] - 2026-06-04


- Fixed UltimateSensor Mini V2 ESP32-C6 UART allocation by disabling serial UART logging in production firmware so LD2412 and LD2450/LD2460 can use the two available hardware UARTs.
- Disabled WiFi fast-connect for UltimateSensor Mini V2 WiFi firmware variants so prebuilt firmware with placeholder WiFi credentials falls back to provisioning more cleanly.
- Removed serial Improv from UltimateSensor Mini V2 production WiFi firmware because ESP32-C6 UARTs are reserved for the two radar modules; fallback AP provisioning remains available.


## [UltimateSensor Mini V1 2.37] - 2026-06-04


- Aligned UltimateSensor Mini V1 cloud payload keys for zone target counts and SPS30 PM size.
- Pointed UltimateSensor Mini V1 Improv setup links to the SmartHomeShop API setup endpoint.
- Fixed GitHub Release note extraction so dated changelog headings publish the matching customer-facing notes.


## [UltimateSensor Mini V2 1.2] - 2026-06-04


- Added SmartHomeShop App cloud firmware variants for UltimateSensor Mini V2 WiFi, Ethernet, LD2450, and optional LD2460 firmware families.
- Fixed UltimateSensor Mini V2 USB logging by routing the ESPHome logger to UART0 and setting the ESP32-C6 flash size explicitly.
- Added LD2450 zone target count IDs for Mini V2 cloud zone sync.
- Fixed GitHub Release note extraction so dated changelog headings publish the matching customer-facing notes.


## [UltimateSensor Mini V2 1.1] - 2026-05-31

- Added optional UltimateSensor Mini V2 LD2460 upgrade firmware variants for customers replacing the LD2450 module while keeping LD2412 installed.
- Split UltimateSensor Mini V2 tracking radar support into standard LD2450 packages and optional LD2460 upgrade firmware packages.
- Documented the Mini V2 LD2460 upgrade policy and pin mapping for WiFi and Ethernet firmware variants.

## [UltimateSensor Mini V1 2.36] - 2026-05-31

- Added four-way firmware switching for UltimateSensor Mini V1 with dedicated Home Assistant `Firmware Variant` and `Firmware Update` controls.
- Added SmartHomeShop App cloud firmware variants for UltimateSensor Mini V1 Basic and Complete, including cloud registration, sensor sync, and cloud manifests.

## [UltimateSensor Mini V2 1.0] - 2026-05-30


- Added UltimateSensor Mini V2 production firmware for ESP32-C6 hardware with WiFi and W5500 Ethernet Basic/Complete variants.
- Added LD2412 and LD2450 occupancy support for UltimateSensor Mini V2.
- Added SPS30 particulate matter support for UltimateSensor Mini V2 Complete variants.
- Added dedicated web flasher manifests for UltimateSensor Mini V2 WiFi and Ethernet firmware.


## [UltimateSensor Mini V1 2.35] - 2026-05-06


- Fix boot audio playback by compiling all speaker media player codecs.


## [UltimateSensor Mini Beta V1 2.35-beta.36] - 2026-04-21


- Added experimental UltimateSensor Mini Basic and Complete beta firmware tracks with on-device Micro Wake Word support.


## [UltimateSensor Mini V1 2.34] - 2026-04-21

### Added

- Customer-facing version history now lives in this repository.
- GitHub Releases will now be published for future firmware versions.

### Changed

- This file is now the public place for customer-facing firmware notes.
