# UltimateSensor Mini for Home Assistant / ESPHome

<p align="center">
  <img src="images/ultimatesensor-mini-inaction-shop.png" alt="UltimateSensor Mini V1" width="360">
  <img src="ultimatesensor-mini-v2/images/ultimatesensor-mini-v2-front.png" alt="UltimateSensor Mini V2" width="360">
</p>

UltimateSensor Mini is a compact all-in-one ESPHome room sensor for Home Assistant. It measures air quality, occupancy, light, temperature, humidity, and optionally particulate matter, with fully local operation by default and optional SmartHomeShop App cloud firmware variants.

Product page: https://ultimatesensor.nl/en/mini

## How It Works

UltimateSensor Mini combines multiple room sensors on one ESP32 device. The ESPHome firmware exposes the measurements directly to Home Assistant and supports local onboarding through captive portal and Improv where available.

The Complete firmware adds SPS30 particulate matter sensing for PM measurements. The Basic firmware uses the same shared configuration without the particulate matter sensor. V2 is sold standard with LD2412 + LD2450. Customers who buy the optional LD2460 upgrade remove/replace the LD2450 module and flash a dedicated `LD2460` firmware variant while leaving LD2412 installed.

## Key Features

- CO2 sensing with SCD41
- Temperature and humidity sensing
- Light sensing with BH1750
- VOC and NOx index sensing with SGP41
- LD2412 close-range mmWave presence sensing on V2
- LD2450 mmWave occupancy and target tracking as the standard V2 tracking radar
- Optional LD2460 target tracking upgrade firmware for V2
- Microphone, speaker, and Home Assistant Voice Assistant support on V1
- RGB front and back lights
- WiFi onboarding with captive portal and Improv where available
- W5500 Ethernet firmware for V2
- Firmware switching between WiFi Basic, WiFi Complete, WiFi Basic Cloud, and WiFi Complete Cloud
- Fully local operation with ESPHome and Home Assistant
- Optional SmartHomeShop App cloud sync firmware
- Optional SPS30 particulate matter sensing in the Complete variant

## Hardware Versions

| Version | Chip | Connectivity | Description |
|---------|------|--------------|-------------|
| V1 | ESP32-S3 | WiFi | UltimateSensor Mini hardware with Basic and Complete firmware variants |
| V2 | ESP32-C6 | WiFi and W5500 Ethernet | UltimateSensor Mini V2 hardware with LD2412 + LD2450 standard, optional LD2460 upgrade firmware, and Basic/Complete variants |

## Variants

We publish local, cloud, and beta firmware variants for V1 hardware. V2 has separate WiFi/Ethernet and LD2450/LD2460 firmware variants.

| Hardware | Variant | Description |
|----------|---------|-------------|
| V1 (ESP32-S3) | Basic | Standard firmware without the SPS30 particulate matter sensor |
| V1 (ESP32-S3) | Complete | Full firmware with SPS30 particulate matter sensing |
| V1 (ESP32-S3) | Basic Cloud | SmartHomeShop App cloud sync firmware without the SPS30 particulate matter sensor |
| V1 (ESP32-S3) | Complete Cloud | SmartHomeShop App cloud sync firmware with SPS30 particulate matter sensing |
| V1 (ESP32-S3) | Beta Basic | Experimental local wake word firmware without the SPS30 particulate matter sensor |
| V1 (ESP32-S3) | Beta Complete | Experimental local wake word firmware with SPS30 particulate matter sensing |
| V2 (ESP32-C6) | WiFi Basic | Standard LD2412 + LD2450 firmware without SPS30 |
| V2 (ESP32-C6) | WiFi Complete | Standard LD2412 + LD2450 firmware with SPS30 |
| V2 (ESP32-C6) | Ethernet Basic | Standard LD2412 + LD2450 W5500 firmware without SPS30 |
| V2 (ESP32-C6) | Ethernet Complete | Standard LD2412 + LD2450 W5500 firmware with SPS30 |
| V2 (ESP32-C6) | WiFi/Ethernet Basic LD2460 | Optional LD2460 upgrade firmware without SPS30 |
| V2 (ESP32-C6) | WiFi/Ethernet Complete LD2460 | Optional LD2460 upgrade firmware with SPS30 |

## Sensors

| Sensor | Description |
|--------|-------------|
| CO2 | Room CO2 concentration |
| Temperature | Environment temperature |
| Humidity | Environment humidity |
| Light | Ambient light level |
| VOC Index | Volatile organic compound index |
| NOx Index | Nitrogen oxide index |
| Occupancy | LD2412 plus tracking radar occupancy detection |
| LD2412 | Close-range mmWave presence fallback on V2 |
| Tracking Radar | LD2450 standard on V2, or LD2460 when the optional upgrade module replaces LD2450 |
| PM1.0 / PM2.5 / PM4.0 / PM10 | Particulate matter measurements in the Complete variant |
| WiFi Signal | WiFi signal strength |
| Uptime | Device uptime |

## Getting Started

1. Power the UltimateSensor Mini with USB-C.
2. Flash the desired firmware with the web flasher or ESPHome CLI.
3. If WiFi is not configured yet, connect to the fallback hotspot.
4. Complete onboarding with captive portal or Improv where available. Mini V2 WiFi uses BLE Improv; Mini V2 serial Improv is not enabled because both ESP32-C6 UARTs are used by the radar modules.
5. Add the device to Home Assistant through the ESPHome integration.
6. For V2 LD2460 upgrades, physically replace/remove the LD2450 module first, leave LD2412 installed, and flash one of the `*-ld2460` firmware files.

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
│   ├── ultimatesensor-mini-basic-cloud.yaml
│   ├── ultimatesensor-mini-complete-cloud.yaml
│   ├── sps30.yaml
│   ├── cloud.yaml
│   ├── cloud-pm.yaml
│   ├── beta-ultimatesensor-mini-common.yaml
│   ├── beta-ultimatesensor-mini-basic.yaml
│   ├── beta-ultimatesensor-mini-complete.yaml
│   └── default_16MB.csv
├── ultimatesensor-mini-v2/          # V2 ESP32-C6 ESPHome configurations
│   ├── base.yaml                    # Shared sensors, LD2412, occupancy logic, API, OTA
│   ├── tracking-ld2450.yaml         # Standard factory tracking package
│   ├── tracking-ld2460.yaml         # Optional LD2460 upgrade package
│   ├── wifi.yaml                    # WiFi connectivity package
│   ├── ethernet.yaml                # W5500 Ethernet connectivity package
│   ├── complete.yaml                # SPS30 particulate matter package
│   ├── ultimatesensor-mini-v2-*-*.yaml
│   └── ultimatesensor-mini-v2-*-*-ld2460.yaml
├── .github/workflows/               # Build and release automation
├── CHANGELOG.md                     # Customer-facing firmware notes
├── SECURITY.md
└── images/
```

## Firmware Downloads

Pre-built firmware manifests are published on the `gh-pages` branch.

- V1 Basic: `ultimatesensor-mini-basic-manifest.json`
- V1 Complete: `ultimatesensor-mini-complete-manifest.json`
- V1 Basic Cloud: `ultimatesensor-mini-basic-cloud-manifest.json`
- V1 Complete Cloud: `ultimatesensor-mini-complete-cloud-manifest.json`
- V1 Beta Basic: `beta-ultimatesensor-mini-basic-manifest.json`
- V1 Beta Complete: `beta-ultimatesensor-mini-complete-manifest.json`
- V2 WiFi Basic: `ultimatesensor-mini-v2-wifi-basic-manifest.json`
- V2 WiFi Complete: `ultimatesensor-mini-v2-wifi-complete-manifest.json`
- V2 Ethernet Basic: `ultimatesensor-mini-v2-ethernet-basic-manifest.json`
- V2 Ethernet Complete: `ultimatesensor-mini-v2-ethernet-complete-manifest.json`
- V2 WiFi Basic LD2460: `ultimatesensor-mini-v2-wifi-basic-ld2460-manifest.json`
- V2 WiFi Complete LD2460: `ultimatesensor-mini-v2-wifi-complete-ld2460-manifest.json`
- V2 Ethernet Basic LD2460: `ultimatesensor-mini-v2-ethernet-basic-ld2460-manifest.json`
- V2 Ethernet Complete LD2460: `ultimatesensor-mini-v2-ethernet-complete-ld2460-manifest.json`

## Contributing

PRs and issues are welcome. Please keep changes modular and follow ESPHome best practices.

If a PR changes firmware behavior or release-visible functionality, add a customer-facing note to [CHANGELOG.md](CHANGELOG.md) under `Unreleased`.

## Support

- Product info and guides: https://ultimatesensor.nl/en/mini
- Store: https://smarthomeshop.io
- Community and support: https://smarthomeshop.io/discord

## License

This project is released under the CC BY-NC 4.0 license. See [license](license).
