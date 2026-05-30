# UltimateSensor Mini for Home Assistant / ESPHome

![UltimateSensor Mini](images/ultimatesensor-mini-inaction-shop.png)

UltimateSensor Mini is a compact all-in-one ESPHome room sensor for Home Assistant. It measures air quality, occupancy, light, temperature, humidity, and optionally particulate matter, with fully local operation by default.

Product page: https://ultimatesensor.nl/en/mini

## How It Works

UltimateSensor Mini combines multiple room sensors on one ESP device. The ESPHome firmware exposes the measurements directly to Home Assistant and supports local onboarding through captive portal and Improv where available.

The Complete firmware adds SPS30 particulate matter sensing for PM measurements. The Basic firmware uses the same shared configuration without the particulate matter sensor.

V1 hardware uses WiFi. V2 hardware adds ESP32-C6 firmware variants for both WiFi and W5500 Ethernet, plus LD2412 and LD2450 occupancy sensing.

## Key Features

- CO2 sensing with SCD41
- Temperature and humidity sensing
- Light sensing with BH1750
- VOC and NOx index sensing with SGP41
- LD2450 mmWave occupancy sensing
- LD2412 presence sensing on V2 hardware
- Microphone, speaker, and Home Assistant Voice Assistant support on V1 hardware
- RGB status lights
- WiFi firmware variants
- W5500 Ethernet firmware variants on V2 hardware
- Fully local operation with ESPHome and Home Assistant
- Optional SPS30 particulate matter sensing in the Complete variant

## Hardware Versions

| Version | Chip | Connectivity | Description |
|---------|------|--------------|-------------|
| V1 | ESP32-S3 | WiFi | UltimateSensor Mini hardware with Basic and Complete firmware variants |
| V2 | ESP32-C6 | WiFi or W5500 Ethernet | UltimateSensor Mini V2 hardware with LD2412, LD2450, and Basic/Complete firmware variants |

## Variants

We publish production firmware variants for V1 and V2 hardware, plus beta firmware for V1 wake word testing.

| Hardware | Variant | Description |
|----------|---------|-------------|
| V1 (ESP32-S3) | Basic | WiFi firmware without the SPS30 particulate matter sensor |
| V1 (ESP32-S3) | Complete | WiFi firmware with SPS30 particulate matter sensing |
| V1 (ESP32-S3) | Beta Basic | Experimental local wake word firmware without the SPS30 particulate matter sensor |
| V1 (ESP32-S3) | Beta Complete | Experimental local wake word firmware with SPS30 particulate matter sensing |
| V2 (ESP32-C6) | WiFi Basic | WiFi firmware without the SPS30 particulate matter sensor |
| V2 (ESP32-C6) | WiFi Complete | WiFi firmware with SPS30 particulate matter sensing |
| V2 (ESP32-C6) | Ethernet Basic | W5500 Ethernet firmware without the SPS30 particulate matter sensor |
| V2 (ESP32-C6) | Ethernet Complete | W5500 Ethernet firmware with SPS30 particulate matter sensing |

## Sensors

| Sensor | Description |
|--------|-------------|
| CO2 | Room CO2 concentration |
| Temperature | Environment temperature |
| Humidity | Environment humidity |
| Light | Ambient light level |
| VOC Index | Volatile organic compound index |
| NOx Index | Nitrogen oxide index |
| Occupancy | mmWave/presence occupancy detection |
| PM1.0 / PM2.5 / PM4.0 / PM10 | Particulate matter measurements in the Complete variant |
| WiFi Signal | WiFi signal strength on WiFi firmware |
| Ethernet IP / MAC | Network diagnostics on Ethernet firmware |
| Uptime | Device uptime |

## Getting Started

1. Power the UltimateSensor Mini.
2. Flash the desired firmware with the web flasher or ESPHome CLI.
3. For WiFi firmware, connect to the fallback hotspot if WiFi is not configured yet.
4. Complete onboarding with captive portal or Improv where available.
5. Add the device to Home Assistant through the ESPHome integration.

Web flasher: https://smarthomeshop.io/firmware
Product page: https://ultimatesensor.nl/en/mini

## Version History

- Customer-facing release notes: [CHANGELOG.md](CHANGELOG.md)
- GitHub Releases: https://github.com/smarthomeshop/ultimatesensor-mini/releases

## Repository Layout

```text
ultimatesensor-mini/
├── ultimatesensor-mini-v1/          # V1 ESPHome configurations
│   ├── ultimatesensor-mini-common.yaml
│   ├── ultimatesensor-mini-basic.yaml
│   ├── ultimatesensor-mini-complete.yaml
│   ├── beta-ultimatesensor-mini-common.yaml
│   ├── beta-ultimatesensor-mini-basic.yaml
│   ├── beta-ultimatesensor-mini-complete.yaml
│   └── default_16MB.csv
├── ultimatesensor-mini-v2/          # V2 ESPHome configurations
│   ├── base.yaml
│   ├── wifi.yaml
│   ├── ethernet.yaml
│   ├── complete.yaml
│   ├── ultimatesensor-mini-v2-wifi-basic.yaml
│   ├── ultimatesensor-mini-v2-wifi-complete.yaml
│   ├── ultimatesensor-mini-v2-ethernet-basic.yaml
│   └── ultimatesensor-mini-v2-ethernet-complete.yaml
├── .github/workflows/               # Build and release automation
├── CHANGELOG.md                     # Customer-facing firmware notes
├── SECURITY.md
└── images/
```

## Firmware Downloads

Pre-built firmware manifests are published on the `gh-pages` branch.

- V1 Basic: `ultimatesensor-mini-basic-manifest.json`
- V1 Complete: `ultimatesensor-mini-complete-manifest.json`
- V1 Beta Basic: `beta-ultimatesensor-mini-basic-manifest.json`
- V1 Beta Complete: `beta-ultimatesensor-mini-complete-manifest.json`
- V2 WiFi Basic: `ultimatesensor-mini-v2-wifi-basic-manifest.json`
- V2 WiFi Complete: `ultimatesensor-mini-v2-wifi-complete-manifest.json`
- V2 Ethernet Basic: `ultimatesensor-mini-v2-ethernet-basic-manifest.json`
- V2 Ethernet Complete: `ultimatesensor-mini-v2-ethernet-complete-manifest.json`

## Contributing

PRs and issues are welcome. Please keep changes modular and follow ESPHome best practices.

If a PR changes firmware behavior or release-visible functionality, add a customer-facing note to [CHANGELOG.md](CHANGELOG.md) under `Unreleased`.

## Support

- Product info and guides: https://ultimatesensor.nl/en/mini
- Store: https://smarthomeshop.io
- Community and support: https://smarthomeshop.io/discord

## License

This project is released under the CC BY-NC 4.0 license. See [license](license).
