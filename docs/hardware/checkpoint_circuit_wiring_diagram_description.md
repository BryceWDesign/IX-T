# Checkpoint Circuit Wiring Diagram Description

This document provides a full verbal schematic and logical flow of the wiring for the checkpoint charging circuit.

## Logical Flow Description

1. **Antenna Array:**
   - Three wideband RF antennas are wired in parallel.
   - The combined output is directed to a bridge rectifier.

2. **Bridge Rectifier:**
   - Constructed using four Schottky diodes (1N5819) in a full-wave configuration.
   - Converts ambient AC-like RF signal to DC.

3. **Boost Converter Input:**
   - DC output from rectifier is fed into the boost converter module.
   - This stage increases voltage to match injection requirements.

4. **Capacitor Bank:**
   - A 1000 µF capacitor is connected directly across the output of the boost converter.
   - Stabilizes voltage output and provides an energy buffer.

5. **MOSFET Switch Circuit:**
   - The positive capacitor terminal connects to the MOSFET drain.
   - The source of the MOSFET connects to the energy loop injection point.
   - The MOSFET gate is controlled by the microcontroller via a GPIO pin, optionally through a resistor.

6. **Sensor Modules:**
   - Voltage sensor is placed across the injection point to monitor potential.
   - Current sensor is in series with the injection point for monitoring amperage.

7. **Microcontroller (ESP32):**
   - Receives data from voltage and current sensors.
   - Sends PWM or logic HIGH/LOW to the MOSFET gate.
   - Enables controlled injection of harvested energy.

## Notes
- All grounds (rectifier, sensors, microcontroller, energy loop) must be tied together for proper circuit function.
- Care should be taken with trace routing to avoid RF interference.
- Use of shielded cables or grounded copper planes is recommended for sensitive sensor lines.

## Optional Enhancements
- Add RF filters or matching networks to antennas for more efficient energy capture.
- Integrate a small display (OLED) to show real-time sensor data.
- Include Wi-Fi telemetry for remote monitoring and logging.

