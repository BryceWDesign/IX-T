# IX-T Validation Protocol

This document defines the experimental validation procedure for testing the IX-T energy loop prototype. It provides a step-by-step process to determine whether ambient energy checkpoints can offset signal decay in a real circuit.

---

## 🎯 Objective

To measure whether the inclusion of ambient energy checkpoints in a decay-prone closed-loop circuit results in a net increase in operational longevity or energy retention compared to an unassisted control loop.

---

## 🧪 Test Setup

### 1. **Baseline Control Circuit**
- Construct a closed-loop circuit using a microcontroller and passive decay model.
- No energy harvesting or external boosts.
- Measure signal/voltage decay over time from an initial known charge.

### 2. **IX-T Enhanced Circuit**
- Same base loop as control.
- Add three ambient energy checkpoints using:
  - RF energy harvester (e.g., Powercast P2110B)
  - Piezoelectric harvester
  - Thermoelectric generator
- Each checkpoint connects to a boost converter and supercapacitor.

---

## 🔧 Test Equipment

- Digital oscilloscope (to monitor voltage decay curves)
- Multichannel datalogger or microcontroller with ADC
- RF signal generator (to simulate ambient RF when needed)
- Thermal plate (to generate small ΔT for thermoelectric test)
- Vibration platform or handheld tool (for piezo test)
- Environmental sensors (optional but recommended)

---

## 📏 Metrics to Capture

| Metric                        | Description                                               |
|------------------------------|-----------------------------------------------------------|
| **Voltage over time**        | For baseline and enhanced loops                           |
| **Energy harvested per checkpoint** | Logged independently                                    |
| **Decay offset**             | Time difference in functional operation before failure    |
| **Ambient condition correlation** | Compare environment vs performance                     |

---

## 📈 Procedure

1. Fully charge baseline circuit. Log voltage every second until failure.
2. Repeat with IX-T enhanced circuit in identical ambient conditions.
3. Repeat both tests across various environments:
   - Normal room
   - RF-rich space (near WiFi or FM source)
   - Vibration platform active
   - Cold-to-warm gradient
4. Capture voltage curves and compare area under curve (AUC) for decay offset.
5. Repeat 3x for each scenario for statistical relevance.

---

## ✅ Success Criteria

- Any statistically significant delay in energy depletion in the IX-T enhanced circuit versus control.
- Positive correlation between ambient conditions and energy harvested.
- Checkpoint logs show verifiable contribution of harvested power to loop integrity.

---

## 🧠 Final Notes

This is a **proof-of-augmentation**, not perpetual motion. We're measuring offset, not generation from nothing. The goal is to validate ambient supplementation in energy-critical low-draw applications.

