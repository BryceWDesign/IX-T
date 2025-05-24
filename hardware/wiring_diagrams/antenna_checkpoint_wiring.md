# Antenna Checkpoint Wiring Diagram and Description

This document describes the wiring layout for connecting ambient RF energy harvesting antennas to the charging subsystem at a checkpoint station. This wiring supports passive recharging of mobile robotics platforms through localized ambient power bursts.

---

## 🧩 Components Used

- 915 MHz ISM band patch or whip antenna  
- RF power detector / rectifier (e.g., LTC3588-1 or equivalent)  
- Supercapacitor (1F to 10F depending on charge rate target)  
- Zener diode for voltage clamping (5.1V)  
- Low-dropout regulator (LDO) or buck converter for output regulation  
- Diode isolation (Schottky) for unidirectional flow to capacitor  
- Optional: Microcontroller for checkpoint handshake signal

---

## 🔌 Schematic Overview

```plaintext
[Antenna]
    |
    v
[RF Rectifier] ---> [Schottky Diode] ---> [Supercapacitor] ---> [LDO Regulator] ---> [Power Out to Drone Pad]
                               |
                               v
                        [Zener Diode to GND]
🔧 Pin-by-Pin Connection Description
| Component      | Pin        | Connects To                       | Notes                         |
| -------------- | ---------- | --------------------------------- | ----------------------------- |
| Antenna        | RF Out     | RF Rectifier IN                   | High-efficiency RF harvesting |
| RF Rectifier   | VOUT       | Schottky Diode anode              | Converts RF to DC             |
| Schottky Diode | Cathode    | Supercapacitor + terminal         | Prevents reverse flow         |
| Supercapacitor | - terminal | System GND                        | Primary storage               |
| Supercapacitor | + terminal | Zener Diode +, LDO input          | Clamp and regulate            |
| Zener Diode    | Cathode    | GND                               | Overvoltage protection        |
| LDO Regulator  | Output     | Drone pad input pins              | Stable 5V or 3.3V             |
| Optional MCU   | GPIO       | Drone ID handshake / ready signal | Logic-only line               |

🔋 Power Behavior
When drone docks, it receives charge passively.

Zener limits spikes, Schottky protects capacitor.

No direct current from drone backflows.

Passive recharge is silent and maintenance-free.

📌 Installation Notes
Mount antenna with clear LOS to RF source (checkpoint router or mesh beacon).

Shield RF rectifier circuit from excessive heat and interference.

Choose capacitor size for burst power profile needed (e.g. flight control board + sensors).

📎 Suggested Real-World Devices
Antenna: Linx ANT-915-CW-HW

RF Rectifier: Analog Devices LTC3588-1

Supercapacitor: Nesscap 10F/2.7V or similar

LDO: TLV755P 5V (Texas Instruments)

Zener: BZX55C5V1

MCU (optional): ATtiny804 or ESP32-S3
