# V1 upgrade guides

This directory contains customer-facing upgrade communication and the release
notes needed when migrating the V1 products to the shared LD2450 tracking
platform.

## Guides

- [Universal V1 products LD2450 update email](v1-products-ld2450-update-en.md)
  covers both UltimateSensor Mini V1 3.0 and UltimateSensor V1 1.13, including
  their different USB-C and OTA installation paths.

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
