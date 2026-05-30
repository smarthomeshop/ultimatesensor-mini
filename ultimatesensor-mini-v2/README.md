# UltimateSensor Mini V2 ESPHome Firmware

V2 targets the ESP32-C6 hardware with LD2412, LD2450, SCD41, BH1750, SGP41, three addressable status LEDs, optional SPS30 particulate matter sensing, and W5500 Ethernet.

The package layout intentionally follows `../ultimatesensor/ultimatesensor-v1`:

| Package | Purpose |
| --- | --- |
| `base.yaml` | Shared ESP32-C6 hardware, sensors, API, OTA, web server, status LEDs, LD2412 and LD2450 |
| `wifi.yaml` | WiFi firmware network stack, captive portal, Improv serial, WiFi diagnostics, W5500 held off/reset |
| `ethernet.yaml` | W5500 Ethernet firmware network stack and Ethernet diagnostics |
| `complete.yaml` | SPS30 particulate matter sensor and PM idle controls |

## Variants

| File | Network | SPS30 |
| --- | --- | --- |
| `ultimatesensor-mini-v2-wifi-basic.yaml` | WiFi | No |
| `ultimatesensor-mini-v2-wifi-complete.yaml` | WiFi | Yes |
| `ultimatesensor-mini-v2-ethernet-basic.yaml` | Ethernet W5500 | No |
| `ultimatesensor-mini-v2-ethernet-complete.yaml` | Ethernet W5500 | Yes |

ESPHome Ethernet and WiFi are kept as separate firmware variants. The WiFi variants keep the W5500 powered off and held in reset. The Ethernet variants power the W5500 and expose Ethernet network info sensors.

## Pin Map

| Function | GPIO |
| --- | --- |
| I2C SDA | GPIO6 |
| I2C SCL | GPIO7 |
| LD2412 TX/RX | GPIO21 / GPIO20 |
| LD2450 TX/RX | GPIO18 / GPIO19 |
| W5500 CLK | GPIO1 |
| W5500 MOSI | GPIO11 |
| W5500 MISO | GPIO10 |
| W5500 CS | GPIO0 |
| W5500 interrupt | GPIO12 |
| W5500 reset | GPIO13 |
| W5500 power enable | GPIO2, inverted |
| Status LED | GPIO23 |
| RGB status LEDs | GPIO22, 3x WS2812/GRB |

## Notes

- Basic variants omit `complete.yaml`.
- Complete variants include `complete.yaml`, which adds the SPS30 at I2C address `0x69`.
- SCD41 default temperature offset is `13.2` based on the local V2 test YAML.
- SCD41 default humidity offset is `3.0` based on the local V2 test YAML.
- The combined `Occupancy` binary sensor turns on when either LD2412 or LD2450 detects presence.
