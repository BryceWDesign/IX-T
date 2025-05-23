# Checkpoint Charging Circuit Component List

This document lists all components required for the assembly of the checkpoint charging circuit.

| Component               | Description                                 | Quantity | Notes                           |
|-------------------------|---------------------------------------------|----------|---------------------------------|
| Wideband RF Antenna      | 100 MHz to 6 GHz frequency range            | 3        | Matched antennas for ambient harvesting |
| Schottky Diode (1N5819) | Low forward voltage, high speed diode       | 4        | For bridge rectifier            |
| Boost Converter Module  | Adjustable output voltage DC-DC converter    | 1        | Prefer high efficiency (>90%)   |
| Electrolytic Capacitor   | 1000 µF, 25V rating                          | 1        | Energy storage capacitor        |
| MOSFET (IRLZ44N)        | Logic level N-channel MOSFET                 | 1        | For energy injection switching  |
| Microcontroller (ESP32) | Wi-Fi enabled microcontroller                | 1        | For PWM control and sensor readout |
| Voltage Sensor Module   | Voltage divider or dedicated sensor          | 1        | For monitoring injection voltage|
| Current Sensor Module   | Hall effect or shunt resistor based sensor   | 1        | For monitoring injection current|
| PCB or Breadboard       | For mounting components                       | 1        | Prototype or custom design      |
| Miscellaneous           | Wires, resistors, connectors, solder         | As needed| For assembly and connections    |

## Notes
- Components are selected for availability and efficiency.
- Exact specifications may vary depending on application environment.
- Alternative components with similar ratings are acceptable.

