# IX-T Hardware Prototype Design

## Objective

Design a feasible hardware prototype that embodies the IX-T concept: a closed-loop ambient energy harvesting system with three checkpoints, each harvesting energy from distinct ambient sources (RF, thermal, vibration). This document details component selection, system architecture, and integration considerations to transition from simulation to a real-world demonstrator.

---

## System Overview

- **Core Controller:** ESP32 microcontroller for low power consumption and rich peripheral support  
- **Energy Harvesting Modules:**  
  - RF Energy Harvester: Antenna array + RF-to-DC rectifier (e.g., Powercast P2110 module)  
  - Thermal Harvester: Thermoelectric generator (TEG) paired with a heat sink and cold sink  
  - Vibration Harvester: Piezoelectric transducer (e.g., Mide Vibration Energy Harvester)  
- **Energy Storage:** Supercapacitors (e.g., 1F, 5.5V) or rechargeable thin-film batteries  
- **Power Management:** Low-dropout regulators (LDO), DC-DC boost/buck converters, and energy management ICs (e.g., TI BQ25570)  
- **Sensing & Telemetry:** Voltage/current sensors (INA219), temperature sensors (DS18B20), and vibration accelerometers (ADXL345) for real-time monitoring  

---

## Architecture Diagram (Conceptual)

```
[Ambient RF] --> [RF Harvester] -->+   
                                  |--> [Energy Storage] --> [ESP32 + Sensors] --> [Checkpoint Logic] --> Loop back  
[Thermal] --> [TEG Module] ------>+   
                                  |  
[Vibration] -> [Piezo Transducer]->+
```

---

## Component Details

| Module           | Suggested Component           | Specs / Notes                                 |
|------------------|------------------------------|-----------------------------------------------|
| Microcontroller  | ESP32 Dev Kit C              | WiFi, Bluetooth, low power sleep modes       |
| RF Harvester     | Powercast P2110 Module       | Harvests RF energy from 915 MHz ISM band     |
| Thermal Harvester | TEC1-12706 TEG              | Typical output ~1-2V under temperature gradient |
| Vibration Harvester | Mide Vibration Energy Harvester | Resonant frequency tuned for ambient vibration |
| Energy Storage   | Maxwell 1F Supercapacitor    | Fast charge/discharge cycles, high power density |
| Power Management | TI BQ25570 energy harvester  | Ultra-low power boost converter with MPPT    |
| Sensors          | INA219 Current/Voltage Sensor | I2C interface, high accuracy                   |
|                  | DS18B20 Temperature Sensor   | Waterproof, digital output                      |
|                  | ADXL345 Accelerometer        | 3-axis, low power, SPI/I2C interface           |

---

## Integration Considerations

- **Form Factor:** Modular PCB design to allow swapping harvesters and sensors  
- **Data Logging:** Onboard storage (SPI flash) or wireless telemetry via ESP32 WiFi/Bluetooth  
- **Power Budget:** Detailed calculations required to balance harvested energy vs system consumption  
- **Environmental:** Protective enclosure with adequate thermal conduction for TEG, vibration isolation/mounting for piezo  
- **Testing Ports:** Accessible test points for voltage/current measurement at each checkpoint  

---

## Development Roadmap

1. Prototype each harvester module separately and characterize output under controlled conditions  
2. Integrate harvesters with power management IC and energy storage, verify charging behavior  
3. Develop checkpoint logic firmware on ESP32 to control energy flow and collect sensor data  
4. Combine modules into a closed-loop circuit and conduct endurance tests  
5. Record and analyze energy balance data to compare with simulation predictions  

---

## References

- Powercast RF Energy Harvesting Datasheet  
- TI BQ25570 Application Notes  
- ESP32 Technical Reference Manual  
- Mide Vibration Energy Harvester Datasheet  
- Thermoelectric Generator (TEG) Fundamentals (Link to relevant papers)

---

This design document forms the basis for physical implementation and iterative development to validate the IX-T concept.

