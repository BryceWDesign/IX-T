# IX-T Energy Harvesting Subsystem Overview

This document provides an overview of the ambient energy harvesting system used in IX-T, with a special focus on the checkpoint recharging infrastructure and antenna-based energy capture. It ties together the electrical, operational, and design considerations necessary to implement this subsystem in real-world conditions.

---

## 🌐 System Architecture

The energy harvesting mechanism in IX-T is split into three primary elements:

1. **High-Gain Ambient Antenna Array (Drone-side)**
2. **Checkpoint Power Transmission Node**
3. **RF-to-DC Conversion and Charging Module (Drone-side)**

---

## 1. High-Gain Ambient Antenna Array

- **Purpose:** Captures ambient RF energy and checkpoint-beamed RF pulses.
- **Design:** Compact folded fractal or helical dipole (selectable depending on range and footprint needs).
- **Specs:**
  - Frequency Band: 915 MHz ISM band (North America) or 2.4 GHz depending on location
  - Gain: 6-12 dBi
  - Size: ≤ 70 mm per axis (folded/compact mount on drone chassis)
  - Materials: Copper foil trace on FR4 / etched flexible PCB

---

## 2. Checkpoint Transmission Node

- **Purpose:** Delivers concentrated RF pulses or inductive EM bursts to recharge drone modules during flyby or stationary perch.
- **Design Notes:**
  - Uses directional high-power antenna or planar inductive coil emitter
  - Can be solar-powered or grid-tethered
  - Pulse width and interval configurable based on drone energy draw
- **Example Configuration:**
  - Transmit Power: 2W pulsed (legal for ISM burst applications)
  - Carrier: 915 MHz (match drone receiver band)
  - Pulse Interval: 10 seconds (on motion sensor trigger)

---

## 3. RF-to-DC Converter Module

- **Purpose:** Converts received RF energy into chargeable DC voltage for battery management subsystem.
- **Design Considerations:**
  - Voltage Output: 3.7V to 4.2V (regulated)
  - Max Input: -5 dBm to +15 dBm (typical ambient levels)
  - Efficiency: 45% at 0 dBm, peaks ~68% at 10 dBm
- **Components:**
  - Matching Network
  - Schottky Diode Rectifier
  - Multi-stage voltage doubler (Greinacher or Cockcroft-Walton)
  - Supercap/battery charge controller (TI BQ25570 or equivalent)

---

## 📐 Integration Summary

| Component              | Location        | Build Source                             |
|------------------------|-----------------|-------------------------------------------|
| Antenna Array          | Drone           | `/hardware/antenna/antenna_module.svg`    |
| RF-to-DC Converter     | Drone           | `/hardware/charging/rf_to_dc_circuit.svg` |
| Checkpoint Transmitter | Environment     | `/hardware/checkpoint/em_tx_node.svg`     |

---

## 🔌 Key Metrics for Validation

| Metric                    | Target       | Notes                              |
|---------------------------|--------------|------------------------------------|
| RF Energy Received        | > 5 dBm      | During checkpoint flyby            |
| Charging Current (DC)     | > 50 mA      | When within 1m of checkpoint node  |
| Battery Voltage Recovery  | +0.1V / min  | From < 3.6V to 4.0V                |
| Idle Harvest Power        | > 1 mW       | From ambient city-level RF only    |

---

## ✅ Replication Instructions

1. Use the provided SVG schematics for antenna and converter builds.
2. Tune antenna with network analyzer (SWR < 2.0).
3. Use a checkpoint TX node emulator (e.g. SDR + amplifier) to simulate energy delivery.
4. Measure charge curve using multimeter and oscilloscope at converter output.

---

> This document is a living part of the IX-T validation stack and directly supports Elon-level reproducibility.

