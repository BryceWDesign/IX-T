# Build Instructions for IX-T Prototype

## Overview

This guide details the step-by-step process to assemble the IX-T energy loop prototype hardware.

## Materials Required

Refer to the Bill of Materials (BOM) for a complete list of components.

## Tools Needed

- Soldering iron and solder
- Wire cutters and strippers
- Multimeter
- Screwdriver set
- Static wrist strap (recommended)

## Assembly Steps

1. **Prepare the PCB**  
   - Inspect PCB for defects  
   - Solder connectors and components as per the schematic (refer to `/docs/schematic.md`)

2. **Install Sensors**  
   - Attach voltage and current sensors to designated checkpoints  
   - Ensure correct orientation and secure connections

3. **Microcontroller Setup**  
   - Mount the RP2040 microcontroller on the PCB  
   - Connect to sensors and power supply as specified

4. **Power Supply Integration**  
   - Connect the regulated power source to the board  
   - Verify voltage levels with a multimeter before powering on

5. **Enclosure Assembly**  
   - Place assembled PCB and components inside the enclosure  
   - Secure all components to prevent movement

6. **Initial Power-On Test**  
   - Power the system and verify microcontroller boots correctly  
   - Check sensor outputs and data logging functionality

## Troubleshooting

- If sensors do not respond, check wiring and solder joints  
- Verify power supply voltages  
- Confirm microcontroller firmware is properly loaded

---

Following these instructions ensures a correctly assembled prototype ready for firmware programming.
