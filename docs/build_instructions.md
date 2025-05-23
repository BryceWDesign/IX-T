# Build Instructions for IX-T Energy Loop Prototype

## Introduction
This guide provides step-by-step instructions to assemble the IX-T energy loop prototype using the listed hardware components.

---

## 1. Preparing Materials
- Verify all hardware components are available.
- Organize tools: soldering iron, wire cutters, screwdrivers, multimeter.

## 2. Constructing the Loop Circuit
- Cut copper wire to form a closed loop of approximately 1 meter in circumference.
- Solder connections securely to avoid resistance points.
- Attach mounting hardware for stability.

## 3. Integrating Energy Checkpoints
- Assemble RF energy harvesting modules per their schematic (refer to `/src/checkpoint_module.py` for logic simulation).
- Connect each checkpoint at evenly spaced intervals on the loop.
- Connect voltage and current sensors before and after each checkpoint.

## 4. Installing Antennas
- Position RF antennas adjacent to each checkpoint.
- Ensure antennas are oriented to maximize ambient RF signal capture.
- Secure antennas and route wiring to corresponding checkpoint modules.

## 5. Sensor and Microcontroller Setup
- Connect sensors to microcontroller analog/digital inputs.
- Program microcontroller with data acquisition and logging firmware.
- Calibrate sensors to ensure accurate readings.

## 6. Power Injection
- Connect the power supply unit to the loop input terminal.
- Apply initial energy injection (refer to `/src/energy_injector.py` for simulation).

## 7. Testing and Validation
- Power on the system and monitor sensor outputs.
- Adjust checkpoint tuning for optimal energy harvesting.
- Record baseline data and observe loop energy sustainment.

## 8. Safety Precautions
- Double-check all connections before powering on.
- Work in a non-conductive area.
- Use personal protective equipment as necessary.

---

## Conclusion
Following these instructions ensures a reproducible and functional prototype build, ready for validation experiments.

