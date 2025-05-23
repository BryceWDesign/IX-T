"""
IX-T Prototype Firmware
Handles sensor data acquisition, processing, and logging.
"""

import time
import machine
import sdcard
import os

# Setup ADC pins for voltage sensors (example GPIOs)
voltage_pins = [machine.ADC(machine.Pin(pin)) for pin in (26, 27, 28)]
# Setup ADC pins for current sensors (example GPIOs)
current_pins = [machine.ADC(machine.Pin(pin)) for pin in (14, 15, 16)]

# Initialize SPI and SD card
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0)
cs = machine.Pin(5, machine.Pin.OUT)
sd = sdcard.SDCard(spi, cs)
os.mount(sd, "/sd")

LOG_FILE = "/sd/ix_t_log.csv"

def read_sensors():
    voltage_values = [adc.read_u16() for adc in voltage_pins]
    current_values = [adc.read_u16() for adc in current_pins]
    return voltage_values, current_values

def log_data(voltage, current):
    timestamp = time.time()
    data_line = f"{timestamp}," + ",".join(map(str, voltage)) + "," + ",".join(map(str, current)) + "\n"
    with open(LOG_FILE, "a") as f:
        f.write(data_line)

def main_loop():
    while True:
        voltage, current = read_sensors()
        log_data(voltage, current)
        time.sleep(1)  # Sampling interval 1 second

if __name__ == "__main__":
    main_loop()
