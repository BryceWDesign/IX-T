# Checkpoint Charging Circuit Component List

This document lists all components required to build the checkpoint charging circuit.

| Component                    | Quantity | Description                                        | Notes                                  |
|------------------------------|----------|--------------------------------------------------|----------------------------------------|
| RF Energy Harvesting Antenna | 3        | Wideband antenna for ambient RF energy harvesting | Custom or commercially available       |
| Schottky Diode Bridge Rectifier | 1        | Low forward voltage diode bridge rectifier        | Example: 1N5819 or MB6S                |
| Boost Converter Module        | 1        | DC-DC step-up converter module                     | Example: XL6009, adjustable output     |
| Electrolytic Capacitor        | 1        | Energy storage capacitor, 1000µF 25V              | Filters and stabilizes output voltage  |
| MOSFET Transistor (N-channel) | 1        | IRFZ44N or similar for energy injection switching | Low Rds(on) for efficiency             |
| Microcontroller (e.g., ESP32) | 1        | Controls MOSFET PWM timing and sensor readings    | High resolution PWM output required    |
| Voltage Sensor (Voltage Divider) | 1      | Voltage sensing circuit to monitor loop voltage   | Resistor divider network                |
| Current Sensor (ACS712)       | 1        | Measures current injected at checkpoint            | 5A version recommended                  |
| Resistors                    | Various  | For voltage dividers and pull-downs                | Values per circuit schematic            |
| Capacitors                  | Various  | For noise filtering and timing                       | Values per schematic                    |
| Miscellaneous (Wires, PCB)  | As needed| For circuit assembly                                 | Custom PCB recommended                  |

