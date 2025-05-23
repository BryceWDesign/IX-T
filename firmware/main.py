"""
IX-T Ambient Energy Harvesting System
Main firmware for Raspberry Pi Pico (MicroPython)
Reads voltage/current from INA219 sensors and logs checkpoint power data.
"""

from machine import I2C, Pin
from ina219 import INA219
import time

# Initialize I2C interface on GPIO 20 (SDA) and 21 (SCL)
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# INA219 sensor I2C addresses (update if needed)
SENSOR_ADDRESSES = [0x40, 0x41, 0x44]

# Initialize sensor instances
sensors = [INA219(i2c, addr) for addr in SENSOR_ADDRESSES]

# Calibration constants (adjust if necessary)
for sensor in sensors:
    sensor.configure()

def log_power():
    """
    Reads voltage and current from each checkpoint sensor,
    calculates power in milliwatts, and prints the results.
    """
    for idx, sensor in enumerate(sensors):
        voltage = sensor.voltage()
        current = sensor.current()  # milliamps
        power = voltage * current / 1000  # milliwatts
        print(f"Checkpoint {idx + 1}: {voltage:.2f} V, {current:.2f} mA, {power:.2f} mW")

def main():
    print("Starting IX-T Ambient Energy Harvesting Monitor...")
    while True:
        log_power()
        time.sleep(5)

if __name__ == "__main__":
    main()
