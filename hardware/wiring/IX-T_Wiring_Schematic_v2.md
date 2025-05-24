# IX-T Drone Wiring Schematic v2

## Overview

This document details the full wiring connections required for the IX-T ambient energy drone prototype. It includes power routing, control logic connections, and sensor interfaces. This version reflects the latest revisions to accommodate checkpoint recharging and BMS integration.

---

## Primary Power System

| Component | Connection | Wire Gauge | Notes |
|----------|------------|------------|-------|
| LiFePO₄ Battery Pack (3S) | To BMS input terminals | 16 AWG | ~11.1V nominal |
| BMS Output | To Power Distribution Board (PDB) | 16 AWG | Protects system |
| PDB | Distributes power to ESCs, FC, and peripherals | — | XT60 or solder pads |

---

## ESC (Electronic Speed Controllers)

| ESC Channel | Motor | Signal Wire (PWM) | Power | Ground |
|-------------|-------|-------------------|--------|--------|
| ESC 1 | Motor 1 | FC PWM CH1 | V+ from PDB | Common Ground |
| ESC 2 | Motor 2 | FC PWM CH2 | V+ from PDB | Common Ground |
| ESC 3 | Motor 3 | FC PWM CH3 | V+ from PDB | Common Ground |
| ESC 4 | Motor 4 | FC PWM CH4 | V+ from PDB | Common Ground |

---

## Flight Controller (FC)

| Signal | Destination | Notes |
|--------|-------------|-------|
| UART1 TX/RX | GPS Module | 3.3V or 5V logic |
| UART2 TX/RX | LoRa Radio | For checkpoint data exchange |
| I2C SDA/SCL | IMU, Barometer | Shared I2C bus |
| PWM1-4 | ESCs 1-4 | Motor control |
| USB | Debug & firmware | Micro USB or USB-C |
| Power Input | From BEC (5V) | 5V regulated power |

---

## Checkpoint Energy Antenna Interface

| Component | Connection | Notes |
|----------|------------|-------|
| Resonant Coil | Rectifier | AC to DC |
| Rectifier | Capacitor bank | Filtering |
| Capacitor bank | BMS charge input | Checkpoint charging circuit |

---

## Sensor Suite (optional)

| Sensor | Interface | Notes |
|--------|-----------|-------|
| GPS (U-blox NEO-M8N) | UART1 | Mounted facing sky |
| Barometer | I2C | Atmospheric pressure |
| IMU | I2C | MPU6050 or ICM20948 |
| Optical Flow Sensor | I2C or SPI | Optional for altitude hold |

---

## Ground Wire Bus

All grounds from ESCs, FC, sensors, and power circuits should share a common ground bus or plane. Poor grounding may cause noisy sensor readings or flight controller resets.

---

## Notes

- Use twisted pairs for signal/power lines where possible.
- Use ferrite beads on sensitive lines (GPS, UART) to suppress EMI.
- Secure all wires to avoid vibration fatigue.
- Ensure proper strain relief on battery leads.

---

## Diagram Reference (Text-Based)

[Battery] --> [BMS] --> [PDB] --> [ESCs]
|
+--> [5V BEC] --> [Flight Controller]
|
+--> [Checkpoint Rectifier & Capacitor Bank] --> [BMS Charge Input]


---

For the actual graphical schematic, see the future upload: `IX-T_Wiring_Diagram_SVG.svg` (to be created separately).
