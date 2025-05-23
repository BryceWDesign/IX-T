"""
IX-T Data Logging Script for Power Sensor Readings

This script collects voltage, current, and power readings from INA219 sensors
at multiple checkpoints in the IX-T prototype and logs them to CSV files
with timestamps for later analysis.

Requirements:
- Python 3.x
- smbus2 library for I2C communication: pip install smbus2
- Compatible INA219 Python library or included minimal driver

Usage:
- Connect INA219 sensors to I2C bus
- Adjust SENSOR_ADDRESSES to match your hardware setup
- Run script: python3 data_logging.py
"""

import time
import csv
from datetime import datetime
from smbus2 import SMBus

# INA219 sensor addresses on I2C bus
SENSOR_ADDRESSES = [0x40, 0x41, 0x44]  # Adjust for each checkpoint sensor

LOG_FILENAME = "ix_t_sensor_log.csv"
LOG_INTERVAL_SEC = 5  # Interval between readings

class INA219:
    """Minimal INA219 driver for reading voltage and current."""
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address
        # Register addresses
        self.REG_BUS_VOLTAGE = 0x02
        self.REG_SHUNT_VOLTAGE = 0x01
        self.REG_CURRENT = 0x04
        self.REG_CALIBRATION = 0x05
        # Initialize calibration (values may need adjustment)
        self.bus.write_word_data(self.address, self.REG_CALIBRATION, 0x2000)

    def read_bus_voltage(self):
        raw = self.bus.read_word_data(self.address, self.REG_BUS_VOLTAGE)
        raw = ((raw & 0xFF) << 8) | (raw >> 8)
        voltage = (raw >> 3) * 4e-3  # 4mV per bit
        return voltage

    def read_shunt_voltage(self):
        raw = self.bus.read_word_data(self.address, self.REG_SHUNT_VOLTAGE)
        raw = ((raw & 0xFF) << 8) | (raw >> 8)
        if raw > 32767:
            raw -= 65536
        voltage = raw * 10e-6  # 10uV per bit
        return voltage

    def read_current(self):
        raw = self.bus.read_word_data(self.address, self.REG_CURRENT)
        raw = ((raw & 0xFF) << 8) | (raw >> 8)
        if raw > 32767:
            raw -= 65536
        current = raw * 0.001  # Example scale: 1mA per bit (adjust as needed)
        return current

def log_sensor_data():
    with SMBus(1) as bus, open(LOG_FILENAME, mode='w', newline='') as csvfile:
        fieldnames = ['timestamp']
        for i in range(len(SENSOR_ADDRESSES)):
            fieldnames += [f'checkpoint_{i+1}_bus_V', f'checkpoint_{i+1}_shunt_V', f'checkpoint_{i+1}_current_mA']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        sensors = [INA219(bus, addr) for addr in SENSOR_ADDRESSES]

        print("Starting data logging to", LOG_FILENAME)
        try:
            while True:
                data = {'timestamp': datetime.now().isoformat()}
                for idx, sensor in enumerate(sensors):
                    data[f'checkpoint_{idx+1}_bus_V'] = round(sensor.read_bus_voltage(), 4)
                    data[f'checkpoint_{idx+1}_shunt_V'] = round(sensor.read_shunt_voltage(), 6)
                    data[f'checkpoint_{idx+1}_current_mA'] = round(sensor.read_current(), 3)
                writer.writerow(data)
                csvfile.flush()
                print(f"Logged data at {data['timestamp']}")
                time.sleep(LOG_INTERVAL_SEC)
        except KeyboardInterrupt:
            print("\nData logging stopped by user.")

if __name__ == "__main__":
    log_sensor_data()
