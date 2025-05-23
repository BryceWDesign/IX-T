# Checkpoint Charging Circuit Assembly Instructions

This document provides step-by-step instructions to assemble the checkpoint charging circuit.

## Tools Needed
- Soldering iron and solder
- Wire cutters and strippers
- Multimeter for testing
- Screwdrivers and pliers

## Assembly Steps

1. **Prepare Antennas:**  
   Mount and arrange the wideband RF antennas to optimize ambient energy reception. Ensure antennas are spaced to reduce interference.

2. **Build Bridge Rectifier:**  
   - Solder four Schottky diodes (1N5819) in a bridge configuration on a PCB or breadboard.  
   - Connect antenna outputs to the AC inputs of the bridge.

3. **Install Boost Converter:**  
   - Connect the DC output from the bridge rectifier to the input of the boost converter module.  
   - Adjust the boost converter output voltage to the target injection voltage (typically 5-12V depending on the energy loop requirements).

4. **Add Energy Storage Capacitor:**  
   - Solder the electrolytic capacitor across the boost converter output terminals for voltage smoothing.

5. **Integrate MOSFET Switching Circuit:**  
   - Connect the MOSFET’s drain to the positive terminal of the capacitor.  
   - Source connects to the checkpoint injection node in the main energy loop.  
   - Gate connects to the microcontroller PWM output pin through a resistor (e.g., 220Ω).

6. **Connect Sensors:**  
   - Wire the voltage and current sensors appropriately to measure the injection point’s voltage and current.  
   - Connect sensor outputs to microcontroller analog/digital input pins.

7. **Program Microcontroller:**  
   - Upload control firmware to the microcontroller to modulate MOSFET switching based on sensor feedback (details in /src/checkpoint_controller.py).

8. **Testing:**  
   - Power up the circuit.  
   - Use a multimeter to verify voltages at key points (antenna outputs, rectifier output, boost converter output, injection node).  
   - Verify microcontroller control signals and sensor readings.

9. **Optimization:**  
   - Adjust boost converter voltage and microcontroller PWM parameters for stable and effective energy injection.

## Safety Notes

- Ensure correct polarity when soldering polarized components.  
- Avoid short circuits during assembly.  
- Use proper shielding to minimize RF noise interference.

