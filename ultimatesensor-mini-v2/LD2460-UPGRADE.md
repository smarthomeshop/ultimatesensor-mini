# Mini V2 LD2460 Upgrade And Calibration

This guide applies only to UltimateSensor Mini V2 hardware fitted with the
optional HLK-LD2460 module. The standard product ships with LD2412 + LD2450.

## Before Installation

1. Disconnect USB-C, Ethernet and PoE power.
2. Remove the LD2450 and leave the LD2412 installed.
3. Install the LD2460 on its dedicated GPIO4/GPIO5 connection.
4. Verify 5V, GND, TX and RX against the PCB labels before restoring power.
5. Flash an UltimateSensor Mini V2 firmware variant whose name ends in
   `LD2460`.

Never move, rotate or reconnect the module while the sensor is powered.

## Physical Orientation

The connector position alone does not define the radar direction. The official
LD2460 side-mount coordinate system is:

- the antenna end points forward into the room and is positive Y;
- positive X is to the right when looking forward from the radar;
- a forward walk should mainly increase Y;
- a left-to-right walk should mainly change X from negative to positive.

If a sideways walk barely changes X but changes Y strongly, the module is
physically oriented on the wrong axis. Power the device off before correcting
the orientation. A 90-degree rotation can therefore be required in a specific
holder, but `90 degrees anticlockwise` is not a universal instruction: it
depends on which way the module was installed initially.

Use the coordinate test above rather than the connector or component text as
the final check. The firmware publishes the LD2460 coordinates without an
automatic 90-degree rotation.

## Installation Mode, Height And Angle

Mini V2 LD2460 firmware requires the radar's `side` installation mode. At every
boot it reads the saved mode and changes it only if necessary. The current mode
is visible as **Tracking Radar Installation Mode**.

When side mode is active, the firmware also reads these saved radar settings:

- **Tracking Radar Installation Height**: actual height above the floor in
  metres;
- **Tracking Radar Installation Angle**: actual wall-mount angle in degrees.

Changing either value sends the documented command to the LD2460 and then
queries both values again. The radar stores these settings across a power
cycle, so they should no longer return to `unknown` after a reboot.

Enter the real measured values. Hi-Link recommends side mounting at `2.2-2.7
m` and an angle of `25-40 degrees`, with `2.6 m` and `30 degrees` as its example.
Mini V2 can detect presence outside that range, but a lower or differently
angled installation can produce less accurate floor coordinates.

## Coordinate Check

After saving the height and angle:

1. Reboot the Mini V2 and confirm that installation mode reads `side`.
2. Confirm that height and angle show the values saved before the reboot.
3. Stand at a measured point directly in front of the sensor.
4. Walk left-to-right and confirm that X spans approximately the walked width.
5. Configure Room Designer zones only after this check succeeds.

Do not expect centimetre-level measurements. The LD2460 report uses 0.1 metre
coordinate steps, and environmental reflections affect the result.

## Duplicate Or Displaced Targets

Mirrors, metal wardrobes, windows and other large reflective surfaces can
produce a stable second target or move the apparent position. This is radar
multipath, not a coordinate rotation that software can fully correct.

For diagnosis:

1. test once with the mirror or reflective surface covered;
2. test with one stationary person and no fan or moving curtain;
3. temporarily remove power from the LD2412 only if support asks you to isolate
   possible radar interaction;
4. keep the LD2412 installed for normal use because combined occupancy uses it
   as the close-range and still-presence fallback.

## References

- [SmartHomeShop LD2460 component](https://github.com/smarthomeshop/ld2460)
- [Hi-Link LD2460 user manual](https://revspace.nl/images/9/9d/HLK-LD2460_2T4R_Multi_Target_Trajectory_Tracking_Module_Manual_V1.1.pdf)
- [Hi-Link LD2460 UART protocol](https://revspace.nl/images/2/2c/HLK-LD2460%E4%B8%B2%E5%8F%A3%E5%8D%8F%E8%AE%AEV1.0_translated.pdf)
