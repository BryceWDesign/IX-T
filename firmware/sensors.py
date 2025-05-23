"""
Sensor Reading Utilities for IX-T Prototype
--------------------------------------------

Functions to read voltage and current sensor data from microcontroller ADC pins.
"""

import machine

def read_voltage(pin_num):
    adc = machine.ADC(pin_num)
    raw_value = adc.read_u16()
    voltage = (raw_value / 65535) * 3.3 * 2  # Assuming voltage divider with ratio 2
    return voltage

def read_current(pin_num):
    adc = machine.ADC(pin_num)
    raw_value = adc.read_u16()
    current = (raw_value / 65535) * 3.3 / 0.1  # Assuming sensor sensitivity 0.1 V/A
    return current
