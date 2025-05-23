# Wiring Guide for IX-T Ambient Energy Harvesting System

This guide provides detailed textual wiring instructions for the energy harvesting circuit, sensors, and microcontroller connections. Follow carefully to ensure correct signal and power flow.

---

## Components Overview

- **Energy Harvesters:** RF module, Thermoelectric Generator (TEG), Piezoelectric Harvester  
- **Sensors:** INA219 voltage/current sensors  
- **Boost Converters:** DC-DC step-up converters  
- **Microcontroller:** Raspberry Pi Pico or Arduino Nano  

---

## 1. Energy Harvester to Sensor Wiring

- For each energy harvester (3 total):  
  - Connect the positive (+) output terminal of the harvester to the VIN+ (input positive) terminal on the INA219 sensor.  
  - Connect the negative (-) terminal of the harvester to the VIN- (input negative) terminal on the INA219 sensor.  
  - Connect the GND of the INA219 sensor to common system ground.

---

## 2. Sensor to Boost Converter Wiring

- For each INA219 sensor output:  
  - Connect VOUT+ (sensor output positive) to the input positive terminal of the boost converter module.  
  - Connect VOUT- (sensor output negative) to the input negative terminal of the boost converter.  
  - Ensure grounds are common and connected.

---

## 3. Boost Converter Output Wiring

- Set each boost converter output voltage to 5V using the onboard potentiometer.  
- Connect each boost converter output positive terminal to the checkpoint input in the energy loop circuit.  
- Connect boost converter output negative terminal to common ground.

---

## 4. Microcontroller Wiring

- Connect sensor SDA and SCL pins to the corresponding I2C pins on the microcontroller:  
  - Raspberry Pi Pico: GPIO 20 (SDA), GPIO 21 (SCL) (example pins)  
  - Arduino Nano: A4 (SDA), A5 (SCL)  

- Connect sensor VCC pins to 3.3V or 5V power rail on microcontroller (as per sensor spec).  
- Connect sensor GND to system ground.

---

## 5. Common Ground and Power

- Establish a single common ground for all components: harvesters, sensors, boost converters, and microcontroller.  
- Power the microcontroller via USB or regulated 5V supply.  
- Ensure power rails are stable and noise-free.

---

## 6. Wire Management

- Use color-coded wires to avoid confusion:  
  - Red for positive voltage lines  
  - Black for ground lines  
  - Other colors for signal lines (SDA, SCL)  

- Keep wiring neat and secure connections with solder or reliable connectors.

---

End of Wiring Guide.

