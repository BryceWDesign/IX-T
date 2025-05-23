# IX-T Hardware Prototype Specification

This document outlines the required components and architecture to construct a physical prototype of the IX-T simulated energy loop system, with three ambient energy checkpoints.

---

## 🎯 Prototype Goal

To demonstrate a sustained energy loop where three distinct checkpoints boost signal strength using ambient energy sources (RF, thermal, vibrational), enabling prolonged circuit activity with no external power input beyond environmental harvesting.

---

## 🧩 Core Components

| Module                         | Description                                                  | Example Part / Vendor                    |
|-------------------------------|--------------------------------------------------------------|------------------------------------------|
| **Microcontroller**           | Central logic & power monitor                                | Adafruit ItsyBitsy M4 / STM32            |
| **Energy Storage**            | Stores and releases energy at each checkpoint                | 10F Supercapacitors, Maxwell/AVX         |
| **RF Harvester**              | Captures RF from ambient environment                         | Powercast P2110B                         |
| **Piezoelectric Generator**   | Converts motion/vibration into energy                        | Mide Volture V25W                        |
| **Thermoelectric Module**     | Harvests energy from heat differentials                     | TEC1-12706 or Laird UltraTEC             |
| **Boost Converter**           | Steps up harvested voltages to usable levels                | TPS61200 Boost IC                        |
| **Energy Monitoring IC**      | Measures decay, recharge, net gain                          | INA219 or MAX17055                       |
| **Oscilloscope + Multimeter** | For testing and signal analysis                              | Rigol DS1054Z / Fluke 87V                |
| **Switching Logic (optional)**| Gates energy flow to simulate checkpoint conditions         | MOSFET array / analog switches           |
| **Enclosure**                 | RF-transparent acrylic or PLA to hold components             | Custom laser-cut / 3D printed            |

---

## 🔁 Circuit Design Summary

- **Ring Layout:** Microcontroller loop with three branching boost checkpoints.
- **Energy Flow:** One-way gating with decay modeling between each checkpoint.
- **Harvest Logic:** Checkpoints activate only if harvested voltage exceeds decay loss.
- **Logging:** Microcontroller records voltage over time to internal storage for analysis.

---

## 📐 Additional Considerations

- Shield part of the setup to simulate RF quiet zones.
- Add programmable dummy loads to mimic device draw (simulating real use).
- Integrate environment sensors (temp, RF strength, vibration) to correlate inputs with checkpoint performance.

---

## 🛠 Assembly Skills Required

- Soldering SMT/through-hole components
- Circuit debugging with multimeter
- Data logging and Python/Arduino serial interfaces
- 3D printing or laser cutting for enclosure design

---

## 💡 Outcome

A measurable proof-of-concept that demonstrates how the IX-T energy loop performs with real-world harvested energy — enabling refinement of simulation parameters and potentially validating the concept’s feasibility in the field.

