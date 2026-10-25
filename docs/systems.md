# Understanding Quiver systems

**Your outcome:** identify the major subsystems and explain how power and commands reach the motors and payload.

Quiver combines an airframe, propulsion assemblies, custom interface and power boards, flight-control hardware, sensors and software. This course uses the documented project as a reference; the issued kit must be checked against the approved release or current devkit.

![System relationships](assets/systems-overview.png)

## Recognise the components

- **Structure:** frame, landing gear, arm attachments and supporting mounts.
- **Powertrain:** motors, electronic speed controllers or integrated propulsion units, arm joints and the removed propellers.
- **Power and wiring:** battery interfaces, distribution, protection, connectors and harnesses.
- **Avionics:** flight controller, sensors and communication hardware.
- **Payloads:** bottom and side attachment hardware, enclosure and associated electrical/data interfaces.
- **Software:** flight firmware, parameters, ground software and simulation.

The Pix32 V6 is a flight-controller module, not a single chip. ArduPilot(Arducopter) is firmware that runs on Pix32 V6 hardware; in SITL, flight-control software runs on a computer with a simulated vehicle.
Note: run with Quiver flight configs.

## Find the right project file

Use the selected BOM and manufacturing drawings to identify parts. Use harness drawings and board documentation for connector identity and pinout. Use firmware documentation only after the physical board and firmware target have been verified.

The reference repository includes attachment-interface CAD under `src/quiver/supporting_structure/attachment_interface`. A drawing image is not a load rating or an approved manufacturing specification.

