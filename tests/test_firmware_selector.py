"""Compile actual OTA routing lambdas and check URL lifetime and variant families."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile
import textwrap
import unittest

ROOT = Path(__file__).resolve().parents[1]
OPTIONS = [
    "WiFi Basic (local)", "WiFi Complete (local)",
    "WiFi Basic + SmartHomeShop App (cloud)", "WiFi Complete + SmartHomeShop App (cloud)",
    "Ethernet Basic (local)", "Ethernet Complete (local)",
    "Ethernet Basic + SmartHomeShop App (cloud)", "Ethernet Complete + SmartHomeShop App (cloud)",
]


def routing_lambda(path):
    source = path.read_text().split("id: sync_selected_firmware_source", 1)[1]
    match = re.search(r"(?m)^      - lambda: \|-\n((?:          [^\n]*(?:\n|$)|\n)+)", source)
    if not match:
        raise AssertionError(f"Missing routing lambda in {path}")
    return textwrap.dedent(match.group(1))


def run_routes(body, options):
    compiler = os.environ.get("CXX") or shutil.which("g++") or shutil.which("clang++")
    if not compiler:
        raise AssertionError("A C++ compiler is required to validate firmware update routes")
    program = '''#include <iostream>
#include <string>
#define ESP_LOGI(...) ((void)0)
#define id(x) x
struct Selector { std::string option; std::string current_option(){return option;} } firmware_selector;
struct Update { const char *url=nullptr; void set_source_url(const char *value){url=value;} } firmware_update;
void select_variant(){
''' + body + '''
}
int main(int argc, char **argv){
  for(int i=1;i<argc;i++){
    firmware_selector.option=argv[i];
    select_variant();
    if(!firmware_update.url)return 2;
    // Read after the lambda returned, just like the ESPHome update component.
    std::cout << firmware_update.url << "\\n";
  }
}
'''
    with tempfile.TemporaryDirectory() as folder:
        source = Path(folder) / "routes.cpp"
        binary = Path(folder) / "routes"
        source.write_text(program)
        compiled = subprocess.run([compiler, "-std=c++17", "-O0", "-fsanitize=address", "-fno-omit-frame-pointer", str(source), "-o", str(binary)], capture_output=True, text=True)
        if compiled.returncode:
            raise AssertionError(compiled.stderr)
        env = {**os.environ, "ASAN_OPTIONS": "detect_leaks=0:detect_stack_use_after_return=1"}
        result = subprocess.run([str(binary), *options], capture_output=True, text=True, env=env)
        if result.returncode:
            raise AssertionError(result.stderr)
        return result.stdout.splitlines()


class FirmwareSelectorTests(unittest.TestCase):
    def test_v2_preserves_network_cloud_tier_and_radar_with_live_url_storage(self):
        source = routing_lambda(ROOT / "ultimatesensor-mini-v2/firmware-selector.yaml")
        for radar in ["", "-ld2460"]:
            with self.subTest(radar=radar):
                body = source.replace("${manifest_base_url}", "https://smarthomeshop.github.io/ultimatesensor-mini").replace("${tracking_suffix}", radar)
                expected = []
                for option in OPTIONS:
                    network = "ethernet" if option.startswith("Ethernet") else "wifi"
                    tier = "complete" if "Complete" in option else "basic"
                    cloud = "-cloud" if "cloud" in option else ""
                    expected.append(f"https://smarthomeshop.github.io/ultimatesensor-mini/ultimatesensor-mini-v2-{network}-{tier}{radar}{cloud}-manifest.json")
                self.assertEqual(run_routes(body, OPTIONS), expected)

    def test_beta_v1_routes_basic_complete_and_cloud_to_existing_build_families(self):
        wrapper = (ROOT / "ultimatesensor-mini-v1/beta-ultimatesensor-mini-common.yaml").read_text()
        substitutions = dict(re.findall(r'^  (\w+_manifest_url): "([^"]+)"$', wrapper, re.M))
        source = routing_lambda(ROOT / "ultimatesensor-mini-v1/ultimatesensor-mini-common.yaml")
        for key in ["basic_manifest_url", "complete_manifest_url", "basic_cloud_manifest_url", "complete_cloud_manifest_url"]:
            self.assertIn(key, substitutions)
            source = source.replace("${" + key + "}", substitutions[key])
        base = "https://smarthomeshop.github.io/ultimatesensor-mini/"
        expected = [base + name + "-manifest.json" for name in [
            "beta-ultimatesensor-mini-basic", "beta-ultimatesensor-mini-complete",
            "ultimatesensor-mini-basic-cloud", "ultimatesensor-mini-complete-cloud",
        ]]
        self.assertEqual(run_routes(source, OPTIONS[:4]), expected)


if __name__ == "__main__":
    unittest.main()
