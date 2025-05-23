"""
IX-T Prototype Main Control Script
----------------------------------

Controls energy checkpoints and monitors system state.

Hardware: Raspberry Pi Pico running MicroPython
"""

import time
from sensors import read_voltage, read_current
from logger import log_data
from config import CHECKPOINTS, SAMPLE_INTERVAL

def main():
    print("Starting IX-T system control loop...")
    while True:
        data_points = []
        for checkpoint in CHECKPOINTS:
            voltage = read_voltage(checkpoint['voltage_pin'])
            current = read_current(checkpoint['current_pin'])
            data = {
                'checkpoint_id': checkpoint['id'],
                'voltage': voltage,
                'current': current,
                'timestamp': time.time()
            }
            data_points.append(data)
            print(f"Checkpoint {checkpoint['id']} Voltage: {voltage:.2f} V, Current: {current:.2f} A")
        log_data(data_points)
        time.sleep(SAMPLE_INTERVAL)

if __name__ == "__main__":
    main()
