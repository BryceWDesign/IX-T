# IX-T Checkpoint Energy Harvesting System: Hardware Specifications

This document outlines the precise components, wiring, and expected output performance for the IX-T system’s ambient energy checkpoints. These modular checkpoints emit low-intensity RF or resonant magnetic fields that are harvested by the drone's antenna arrays during flight or hover.

---

## 🧩 Purpose

To provide autonomous mid-flight or staged charging locations for IX-T drones using wireless non-contact energy transfer at defined coordinates. Enables indefinite operation across loops.

---

## 📦 Hardware Components per Checkpoint

| Component                       | Model / Part No.                    | Quantity | Description                              |
|-------------------------------|-------------------------------------|----------|------------------------------------------|
| RF Transmitter Module         | Powercast TX91501-3W                | 1        | 915 MHz RF energy emitter                |
| Directional Antenna           | L-Com HG915RD-120                   | 1        | 120° sector patch for targeting drone    |
| Boost Converter               | Pololu U3V70A                       | 1        | Ensures stable 5V or 12V output          |
| Power Supply (AC-DC)          | MeanWell RS-25-5 or RS-25-12        | 1        | Converts wall AC to 5V/12V DC            |
| Microcontroller (optional)    | ESP32-C3 Mini DevKit                | 1        | Allows remote monitoring + beacon ID     |
| Enclosure (IP-rated)          | Hammond 1554 or 1555 series         | 1        | Outdoor protective housing               |
| Passive Cooling Heatsink      | Generic 30x30mm aluminum fins       | 1        | Avoid thermal drift in transmitter       |

---

## ⚡ Electrical Diagram

While image-based schematics are not provided, here is a wiring logic description:

1. **AC In → MeanWell RS-25-12 → Pololu Boost Converter**  
   → RF Transmitter (TX91501) → Directional Antenna

2. Optional:  
   AC In → 5V Line → ESP32 → WiFi or BLE Beacon + MQTT Signal

3. Antenna faces drone pass-through lane (preset GPS corridor or marker).

---

## 📐 Installation Notes

- Elevation: 1.5 to 3 meters height from ground  
- Orientation: Antenna face pointed toward approach vector  
- Spacing: One checkpoint every 20–40 meters for urban loop; 60–120m for open fields  
- Redundant overlapping sectors recommended

---

## 🔋 Output Profile

| Distance (m) | Received Power (mW) |
|--------------|----------------------|
| 1m           | 850 mW               |
| 2m           | ~400 mW              |
| 5m           | ~100 mW              |
| 10m          | ~10-20 mW            |

> Real output will depend on angle of approach, interference, and harvesting circuit efficiency onboard drone.

---

## 🛠 Integration with Drone

Drone receives checkpoint energy via:

- Rectifying antenna + resonant tuned circuit  
- Supercapacitor buffer → boost converter → BMS microcontroller

Checkpoint energy used for trickle charge, stabilization, or failsafe recharge.

---

## 📋 Future Optimization

- Directional antenna tilt auto-calibration  
- Drone-side GPS handshake to activate checkpoint beacon burst  
- Multiple frequency layers (915 MHz + 433 MHz backup)

---

