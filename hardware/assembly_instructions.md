# Assembly Instructions for IX-T Ambient Energy Harvesting System

This document provides a step-by-step guide to assembling the hardware components for the IX-T system. Follow these instructions carefully to ensure correct construction and functionality.

---

## Tools Required

- Soldering station and solder  
- Wire cutters and strippers  
- Screwdrivers and small pliers  
- Multimeter for testing connections  

---

## Step 1: Prepare Energy Harvester Modules

1. **RF Energy Harvester Modules:**  
   - Unpack modules and verify pinouts for power output, ground, and signal.  
   - Solder short wires to the output terminals if not pre-wired.

2. **Thermoelectric Generators (TEGs):**  
   - Mount TEGs on heatsink plates if provided or available.  
   - Connect leads to wires, ensuring polarity is marked.

3. **Piezoelectric Harvesters:**  
   - Attach leads securely to piezo elements.  
   - Use strain relief or hot glue to protect connections from mechanical stress.

---

## Step 2: Microcontroller Setup

1. **Select your microcontroller board (Raspberry Pi Pico or Arduino Nano recommended).**

2. **Connect Voltage/Current Sensor Modules:**  
   - Wire INA219 sensor modules between each energy harvester output and the boost converter input.  
   - Connect I2C pins (SCL, SDA) to microcontroller according to its pinout.

3. **Connect Boost Converters:**  
   - Connect energy harvester outputs (through sensors) to boost converter inputs.  
   - Set boost converter output voltage to 5V using the onboard potentiometer.

4. **Connect boost converter outputs to the energy circuit loop inputs (the checkpoints).**

---

## Step 3: Wiring the Closed-Loop Circuit

1. Use insulated wires to create the circuit loop connecting the energy harvesters through boost converters and sensors.

2. Ensure proper grounding of all components to prevent electrical noise and interference.

3. Use connectors or solder joints to secure all wiring.

4. Keep wire lengths short to minimize resistance and energy loss.

---

## Step 4: Enclosure Preparation

1. Choose an enclosure large enough to house all components with space for wiring.

2. Drill holes or slots for connectors, sensors, and airflow if needed for thermal harvesters.

3. Mount components securely inside the enclosure using screws, brackets, or adhesive as appropriate.

---

## Step 5: Final Checks

1. Inspect all solder joints and connections for cold joints or shorts.

2. Verify correct polarity on all power lines.

3. Use a multimeter to test voltage at various points in the circuit.

---

## Step 6: Powering On and Firmware Upload

1. Connect the microcontroller to your computer via USB.

2. Follow firmware programming instructions (see `/firmware/programming_guide.md`) to upload control and monitoring code.

3. Power the system and monitor startup behavior.

---

## Tips & Warnings

- Double-check all connections before powering the system.

- Avoid short circuits; use insulating materials where wires cross or run close.

- Work in a static-free environment to protect sensitive components.

---

End of Assembly Instructions.

