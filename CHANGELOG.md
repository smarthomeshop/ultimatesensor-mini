# Changelog

All notable customer-facing firmware changes for UltimateSensor Mini are tracked in this file.

This changelog starts on 2026-04-21. Earlier firmware versions existed before that date, but they were not tracked in a customer-facing changelog.

## [Unreleased]

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
