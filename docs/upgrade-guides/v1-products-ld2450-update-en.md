# Email: UltimateSensor V1 firmware and LD2450 update

## Subject

Important firmware update for UltimateSensor V1 products

## Email

Dear customer,

New firmware is available for the **UltimateSensor Mini V1** and
**UltimateSensor V1**. Both products now use our improved LD2450 tracking with:

- live position tracking for up to three people;
- four polygon zones and two exclusion zones;
- two virtual entry lines;
- people counting.

Existing rectangular zones are not converted automatically. Please save your
current zone settings before updating and configure the new polygon zones
afterwards.

### UltimateSensor Mini V1

Firmware **2.43 was released on July 27, 2026**. Install it once via USB-C at
[smarthomeshop.io/firmware](https://smarthomeshop.io/firmware).

**Do not install this specific Mini V1 update through Home Assistant or OTA.**
The internal platform changes from Arduino to ESP-IDF, so a full USB-C
installation is required. Future updates will work wirelessly again.

Select **UltimateSensor Mini V1**, followed by your Basic/Complete and local
Home Assistant/SmartHomeShop App variant. This also applies to former Mini V1
beta users.

### UltimateSensor V1

Update normally to firmware **1.13** using the firmware update in Home
Assistant. The new LD2450 tracking was introduced in version **1.11 on July
24, 2026** and is included in 1.13. A USB-C installation is not required for
this model.

After updating, check your presence automations and redraw your zones using the
SmartHomeShop Room Designer.

Documentation is available at
[docs.smarthomeshop.io](https://docs.smarthomeshop.io). If you have any
questions, please join our
[SmartHomeShop Discord community](https://smarthomeshop.io/discord). We will
be happy to help you there.

Kind regards,

SmartHomeShop

## Internal release check

Before sending this email, verify that:

- all four Mini V1 2.43 firmware variants are available;
- UltimateSensor V1 1.13 is available through its firmware update;
- a real Mini V1 running 2.42 has been upgraded successfully via USB-C;
- WiFi, Home Assistant, sensors, audio and LD2450 tracking work after the Mini
  V1 upgrade.
