# Full Build Walkthrough: Ambient Energy Loop Checkpoint System

This document provides complete, step-by-step guidance to physically build the checkpoint-based ambient energy loop system.

---

## Tools and Materials Required

### Core Components
- 3 × RF Wideband Antennas (868 MHz–2.4 GHz)
- 3 × Bridge Rectifier Modules (or 12 × 1N5819 Schottky Diodes)
- 3 × Boost Converter Modules (e.g., MT3608)
- 3 × Supercapacitors (1F 5.5V) or 1000 µF electrolytic capacitors
- 3 × N-Channel MOSFETs (e.g., IRFZ44N)
- 3 × Current Sensors (e.g., ACS712)
- 3 × Voltage Divider Circuits
- 1 × ESP32 or similar microcontroller
- Jumper wires, breadboard or custom PCB, 3.3V regulator (if not onboard), power source for initialization

### Tools
- Soldering iron and solder
- Wire strippers and snips
- Multimeter and oscilloscope (optional but recommended)
- Small screwdriver set
- 3D printer (optional, for housing)

---

## Step-by-Step Build Guide

### 1. **Prepare the Energy Harvesting Units**
- Connect three antennas to individual bridge rectifiers.
- Confirm correct polarity and continuity with a multimeter.
- Solder outputs of rectifiers to boost converter inputs.
- Tune boost converter output to ~5V (adjustable for application).

### 2. **Integrate Capacitor and MOSFET**
- Attach a capacitor across each boost converter’s output.
- Solder the positive terminal of each capacitor to the drain of a MOSFET.
- Connect the source of the MOSFET to the loop injection point.
- Add gate resistor (220Ω) between ESP32 GPIO and gate terminal.

### 3. **Sensor Integration**
- Voltage divider (100kΩ/10kΩ) across injection point to monitor voltage.
- Insert ACS712 current sensor in series with injection output.
- Connect analog outputs of both sensors to ESP32.

### 4. **Controller Wiring**
- ESP32 is powered via USB or dedicated 3.3V source.
- Wire up sensors and MOSFET gate controls to ESP32 GPIO.
- Confirm common ground between ESP32 and all checkpoint modules.

### 5. **Testing the Circuit**
- Run validation script (see `/scripts/checkpoint_diagnostics.py`) to test signal outputs.
- Use multimeter to confirm correct boost converter and sensor readings.

### 6. **System Calibration and Injection Logic**
- Upload firmware to ESP32 (`firmware/checkpoint_control.py`).
- Observe voltage/current behavior using serial output or dashboard.
- Adjust capacitor values or converter voltage as needed for optimal injection.

---

## Assembly Best Practices

- Route all antenna wires away from signal-carrying sensor cables.
- Use heat-shrink tubing and enclosures to protect modules.
- Consider shielding sensitive analog lines from interference.
- Secure all components to avoid mechanical stress.

---

## Safety Notes
- Although voltages are generally low, boost converters can produce significant current—avoid shorts.
- Capacitors can retain charge—discharge safely before handling.
- This prototype is not certified for public deployment.

---

## Estimated Build Time
- Basic prototype: 4–6 hours
- Final system with all checkpoints: 8–12 hours

---

