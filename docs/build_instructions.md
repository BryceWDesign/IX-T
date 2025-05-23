# Build Instructions for IX-T Energy Loop Prototype

## Required Materials and Components

| Component              | Quantity | Description                             | Approximate Cost (USD) |
|------------------------|----------|-------------------------------------|-----------------------|
| Microcontroller Board  | 1        | Raspberry Pi Pico or equivalent       | 10                    |
| Voltage Sensors (ADC)  | 3        | Analog voltage sensors (e.g., INA219) | 15                    |
| Current Sensors (ADC)  | 3        | Hall effect or shunt resistors        | 20                    |
| SD Card Module         | 1        | For data logging                      | 10                    |
| Breadboard & Wiring    | As needed| Jumper wires, resistors, capacitors   | 10                    |
| Power Supply           | 1        | Stable 5V DC power source              | 15                    |

## Tools Needed

- Soldering iron and solder  
- Multimeter  
- Wire cutters and strippers  
- Computer for programming the microcontroller  

## Assembly Steps

1. **Sensor Setup**  
   - Connect voltage sensors to designated ADC pins on the microcontroller.  
   - Connect current sensors similarly ensuring correct polarity.

2. **SD Card Integration**  
   - Wire the SPI interface between microcontroller and SD card module.  
   - Confirm mounting and file write capabilities with sample code.

3. **Power Supply**  
   - Connect and test the 5V power supply for stable voltage output.  
   - Ensure proper grounding across the system.

4. **Programming**  
   - Flash the provided firmware (`main.py`) to the microcontroller using appropriate tools.  
   - Verify sensor readings via serial output before enabling data logging.

5. **Testing**  
   - Run the system and confirm data is logged correctly on the SD card.  
   - Perform baseline measurements before activating checkpoint energy inputs.

## Notes

- Use caution when handling electronics and ensure proper insulation.  
- Follow all safety protocols regarding power supply connections.

---

Following these steps will produce a functioning IX-T energy loop prototype ready for validation testing.
