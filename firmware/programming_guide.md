# Firmware Programming Guide for IX-T Ambient Energy Harvesting System

This guide provides instructions to program the microcontroller to monitor and manage the energy harvesting checkpoints. The example firmware uses Python (MicroPython) for Raspberry Pi Pico or C++ for Arduino Nano.

---

## 1. Prerequisites

- Microcontroller board (Raspberry Pi Pico or Arduino Nano)  
- USB cable to connect microcontroller to PC  
- Installed development environment:  
  - Raspberry Pi Pico: Thonny IDE with MicroPython support  
  - Arduino Nano: Arduino IDE  

- INA219 sensor libraries installed:  
  - MicroPython INA219 library for Pico  
  - Adafruit INA219 Arduino library for Nano  

---

## 2. Setting up Development Environment

### Raspberry Pi Pico (MicroPython)

1. Install Thonny IDE from https://thonny.org/  
2. Connect Pico and select MicroPython (Raspberry Pi Pico) interpreter in Thonny.  
3. Install INA219 MicroPython library (e.g., `ina219.py`) in your project directory.

### Arduino Nano (C++)

1. Install Arduino IDE from https://www.arduino.cc/en/software  
2. Install Adafruit INA219 library via Library Manager.  
3. Select Arduino Nano board and COM port.

---

## 3. Uploading Firmware Code

- Sample code templates provided in `/firmware/` directory (`main.py` for Pico, `main.ino` for Nano).  
- Code reads voltage and current from INA219 sensors, calculates power, and logs data.  
- Code can optionally control power checkpoints or signal alarms.

---

## 4. Example Firmware Outline (Raspberry Pi Pico)

```python
from machine import I2C, Pin
from ina219 import INA219
import time

i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# Addresses of INA219 sensors (may vary)
sensor_addresses = [0x40, 0x41, 0x44]

sensors = [INA219(i2c, addr) for addr in sensor_addresses]

def log_power():
    for i, sensor in enumerate(sensors):
        voltage = sensor.voltage()
        current = sensor.current()
        power = voltage * current / 1000  # milliwatts
        print(f"Checkpoint {i+1}: {voltage:.2f} V, {current:.2f} mA, {power:.2f} mW")

while True:
    log_power()
    time.sleep(5)
```

---

## 5. Example Firmware Outline (Arduino Nano)

```cpp
#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 sensor1(0x40);
Adafruit_INA219 sensor2(0x41);
Adafruit_INA219 sensor3(0x44);

void setup() {
  Serial.begin(115200);
  sensor1.begin();
  sensor2.begin();
  sensor3.begin();
}

void loop() {
  float voltage1 = sensor1.getBusVoltage_V();
  float current1 = sensor1.getCurrent_mA();
  float power1 = voltage1 * current1 / 1000;

  Serial.print("Checkpoint 1: ");
  Serial.print(voltage1); Serial.print(" V, ");
  Serial.print(current1); Serial.print(" mA, ");
  Serial.print(power1); Serial.println(" mW");

  // Repeat for sensor2 and sensor3...

  delay(5000);
}
```

---

## 6. Customization and Expansion

- Add data logging to SD card or transmit via wireless modules (e.g., ESP8266).  
- Implement automatic checkpoint adjustments or feedback control.  
- Integrate with visualization dashboard via serial or network.

---

End of Firmware Programming Guide.

