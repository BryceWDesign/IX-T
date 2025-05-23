# Checkpoint Charging Circuit Build Instructions

This guide provides step-by-step instructions to assemble the checkpoint charging circuit.

## Tools Required
- Soldering iron and solder
- Wire cutters/strippers
- Multimeter
- Screwdriver set
- Breadboard or PCB for prototyping

## Assembly Steps

1. **Prepare the Antenna Array:**
   - Arrange three wideband RF antennas.
   - Connect the antenna terminals in parallel or series as per schematic.
   - Route the combined RF signals to the input of the rectifier.

2. **Build the Rectifier Circuit:**
   - Solder the Schottky diodes into a bridge rectifier configuration.
   - Connect antenna outputs to AC input terminals of the rectifier.
   - Ensure polarity is correct for DC outputs.

3. **Connect Boost Converter:**
   - Wire the rectifier DC outputs to the boost converter input (VIN+, VIN-).
   - Adjust the boost converter output voltage to desired charging voltage (e.g., 5V).
   - Connect the output to the energy storage capacitor.

4. **Install Energy Storage Capacitor:**
   - Connect the capacitor terminals to the boost converter output.
   - Ensure correct polarity and secure the capacitor.

5. **MOSFET Wiring:**
   - Connect the MOSFET Drain to the energy loop injection point.
   - Connect the Source to ground.
   - Connect the Gate to the microcontroller PWM output pin.

6. **Microcontroller Setup:**
   - Program the microcontroller for PWM control of MOSFET.
   - Connect voltage and current sensors to the microcontroller ADC pins.
   - Implement feedback control to optimize energy injection.

7. **Testing:**
   - Power up the circuit with test voltage.
   - Verify the boost converter output voltage.
   - Use multimeter to verify voltages at key points.
   - Check PWM switching and sensor readings on microcontroller serial output.

## Safety Notes
- Ensure no short circuits before powering.
- Use appropriate voltage and current ratings for all components.
- Always discharge capacitors before handling.

