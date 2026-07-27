# V1 upgrade guides

This directory contains customer-facing upgrade communication and the release
notes needed when migrating the V1 products to the shared LD2450 tracking
platform.

## Guides

- [UltimateSensor Mini V1 2.42/beta to production 2.43](mini-v1-2-42-to-2-43-usb-nl.md)
  is ready for the V1 2.43 production release after the firmware has passed the
  release checklist in that document.

## Important release distinction

The UltimateSensor Mini V1 beta runtime has been integrated into production
while preserving:

- `smarthomeshop.ultimatesensor_mini` as the ESPHome project name;
- `ultimatesensor-mini` as the default device name;
- Basic and Complete firmware;
- local and SmartHomeShop App cloud firmware;
- the production firmware selector and OTA manifests;
- stable customer-facing entity names wherever possible.

The shared LD2450 packages add native target tracking, four polygon zones, two
exclusion zones, two entry lines and people counting. Existing rectangular
zone settings are not automatically converted to polygons.
