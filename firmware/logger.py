"""
Data Logging Module for IX-T Prototype
--------------------------------------

Handles writing checkpoint sensor data to onboard SD card for later analysis.
"""

import os
import time

LOG_FILE = "/sd/ix_t_log.csv"

def initialize_log():
    if not os.path.exists("/sd"):
        raise RuntimeError("SD card not mounted. Please mount before logging.")
    if not os.path.isfile(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("timestamp,checkpoint_id,voltage,current\n")

def log_data(data_points):
    with open(LOG_FILE, "a") as f:
        for data in data_points:
            line = f"{data['timestamp']},{data['checkpoint_id']},{data['voltage']:.3f},{data['current']:.3f}\n"
            f.write(line)
