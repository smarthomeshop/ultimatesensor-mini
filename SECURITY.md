# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest (main) | ✅ |
| Older releases | ❌ |

We recommend always running the latest firmware version via OTA update.

## Reporting a Vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Instead, use GitHub's private vulnerability reporting:
**[Report a vulnerability](https://github.com/smarthomeshop/ultimatesensor-mini/security)**

We aim to respond within **7 days** and will keep you updated on the fix progress.

## Known Security Considerations

### LD2450 Bluetooth
The LD2450 mmWave radar sensor exposes a Bluetooth interface used by the HLKRadarTool app for configuration. Anyone physically within Bluetooth range (~10m) could potentially connect and modify radar settings such as detection zones or sensitivity.

**Mitigation:** A toggle switch is available under the device's Configuration entities in Home Assistant to disable LD2450 Bluetooth when not actively configuring the sensor. It is recommended to keep Bluetooth disabled during normal operation.

### OTA Updates
Over-the-air firmware updates are protected by ESPHome's built-in OTA mechanism. Ensure your Home Assistant instance and local network are secured to prevent unauthorized firmware updates.

### Home Assistant API
The device communicates with Home Assistant over an encrypted API. Ensure your Home Assistant API key (configured via ESPHome) is kept private and not shared or committed to version control.

### No Credentials in Config Files
WiFi credentials, API keys, and OTA passwords should never be hardcoded in the YAML configuration files. Use ESPHome's `secrets.yaml` file for all sensitive values and ensure it is excluded from version control (`.gitignore`).

## Out of Scope

- Vulnerabilities in ESPHome, Home Assistant, or other upstream dependencies — please report those to their respective projects
- Issues requiring physical access to the device's internals
- Theoretical attacks with no practical exploit path
