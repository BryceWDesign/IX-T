"""
Configuration and Calibration for IX-T Prototype Firmware
---------------------------------------------------------

Define constants and calibration parameters for sensors and checkpoints.
"""

# Sampling interval in seconds
SAMPLE_INTERVAL = 5

# Checkpoint definitions with ADC pins
CHECKPOINTS = [
    {'id': 1, 'voltage_pin': 26, 'current_pin': 27},
    {'id': 2, 'voltage_pin': 28, 'current_pin': 29},
    {'id': 3, 'voltage_pin': 30, 'current_pin': 31},
]

# Calibration constants (to be updated with actual measurements)
VOLTAGE_DIVIDER_RATIO = 2.0
CURRENT_SENSOR_SENSITIVITY = 0.1  # Volts per Amp
