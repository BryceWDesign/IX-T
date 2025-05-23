"""
IX-T Energy Loop Validation Data Analysis Script

This script processes sensor data logs to calculate success metrics defined in
validation/success_metrics.md and generates a summary report.
"""

import pandas as pd
import numpy as np

# Load sensor data CSV (columns: timestamp, checkpoint_id, voltage, current)
data = pd.read_csv('data/sensor_log.csv', parse_dates=['timestamp'])

# Calculate power per measurement (P = V * I)
data['power'] = data['voltage'] * data['current']

# Calculate total energy input and output (Joules)
# Assuming sampling interval in seconds is uniform and equal to delta_t
delta_t = (data['timestamp'].iloc[1] - data['timestamp'].iloc[0]).total_seconds()

# Separate input and output by checkpoint_id
input_power = data[data['checkpoint_id'] == 'input']['power'].sum() * delta_t
output_power = data[data['checkpoint_id'] == 'output']['power'].sum() * delta_t

# Energy Sustainment Ratio (ESR)
esr = output_power / input_power if input_power > 0 else np.nan

# Checkpoint Harvesting Efficiency (CHE)
total_losses = input_power - output_power if input_power > output_power else 0
energy_harvested = data[data['checkpoint_id'].str.contains('checkpoint')]['power'].sum() * delta_t
che = (energy_harvested / total_losses) * 100 if total_losses > 0 else np.nan

# Stability Index (SI)
power_mean = data['power'].mean()
power_variance = data['power'].var()
si = power_variance / power_mean if power_mean > 0 else np.nan

# Autonomous Operation Time (AOT)
# Define AOT as time span with output power >= input power after initial injection
threshold = input_power  # Simplified assumption for demonstration
aot = (data[data['power'] >= threshold]['timestamp'].max() - data['timestamp'].min()).total_seconds() / 3600

# Generate summary report
report = f"""
IX-T Energy Loop Validation Summary Report

Energy Sustainment Ratio (ESR): {esr:.3f}
Checkpoint Harvesting Efficiency (CHE): {che:.2f}%
Stability Index (SI): {si:.4f}
Autonomous Operation Time (AOT): {aot:.2f} hours

"""

print(report)

# Save report to file
with open('validation_report.txt', 'w') as f:
    f.write(report)
