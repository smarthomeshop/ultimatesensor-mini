## UltimateSensor Mini for Home Assistant / ESPHome

![UltimateSensor Mini](images/ultimatesensor-mini-inaction-shop.png)

[![CI – Build & Publish](https://github.com/smarthomeshop/ultimatesensor-mini/actions/workflows/publish.yml/badge.svg)](https://github.com/smarthomeshop/ultimatesensor-mini/actions/workflows/publish.yml)

UltimateSensor Mini is a compact, all‑in‑one room sensor powered by ESPHome. It runs fully local (no cloud) and integrates seamlessly with Home Assistant.

- **Connectivity**: Wi‑Fi (no Ethernet/PoE)
- **Sensors**: CO₂ (SCD41), temperature, humidity, light (BH1750), VOC/NOx (SGP41), particulate matter (SPS30, Complete variant)
- **Audio & VA**: microphone and speaker with Voice Assistant
- **Provisioning**: Improv over BLE/Serial and captive portal

More info: `https://ultimatesensor.nl/en/mini`

### Variants

- **Basic**: core features without the SPS30 particulate sensor
  - YAML: `ultimatesensor-mini-v1/ultimatesensor-mini-basic.yaml`
  - Dashboard import: `github://smarthomeshop/ultimatesensor-mini/ultimatesensor-mini-v1/ultimatesensor-mini-basic.yaml@main`
  - OTA manifest: `https://smarthomeshop.github.io/ultimatesensor-mini/ultimatesensor-mini-basic-manifest.json`

- **Complete**: everything in Basic + SPS30 particulate sensor
  - YAML: `ultimatesensor-mini-v1/ultimatesensor-mini-complete.yaml`
  - Dashboard import: `github://smarthomeshop/ultimatesensor-mini/ultimatesensor-mini-v1/ultimatesensor-mini-complete.yaml@main`
  - OTA manifest: `https://smarthomeshop.github.io/ultimatesensor-mini/ultimatesensor-mini-complete-manifest.json`

### Quick start

1. Mount/place the device and power it via USB‑C.
2. Flash firmware:
   - Via GitHub Pages manifest (OTA or your own Web Tools page), or
   - Locally with ESPHome CLI: `esphome run ultimatesensor-mini-v1/ultimatesensor-mini-basic.yaml`
3. Provisioning: use Improv (BLE/Serial) or the captive portal to set up Wi‑Fi.

### OTA updates in ESPHome

Both variants expose an `update` entity (HTTP manifest). The YAML uses substitutions similar to:

- `wifi_fast_connect: "true"`
- `name_add_mac_suffix: true`
- `update_manifest_url: <variant‑specific manifest URL>`

### Repository layout

- `ultimatesensor-mini-v1/` — ESPHome configurations (common + Basic/Complete variants)
- `.github/workflows/` — CI that builds and publishes binaries and manifests to `gh-pages`
- `ceilsense/` — reference project with a similar setup (Wi‑Fi/Ethernet variants)
- `gh-pages` branch — public firmware and manifests (for OTA/ESP Web Tools)

### CI / version injection

- GitHub Actions build on each commit/tag and publish to `gh-pages`.
- Version injection: during CI `ultimatesensor_mini_software_version` is set to the tag version (`vX.Y.Z` → `X.Y.Z`) or `dev-<shortsha>`.

### Contributing & support

- PRs and issues are welcome.
- Community & support (Discord): `https://smarthomeshop.io/discord`

### License

This project is released under [CC BY‑NC 4.0](license).