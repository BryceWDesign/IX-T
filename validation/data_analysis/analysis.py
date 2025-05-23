"""
IX-T Data Analysis Script

Processes sensor log CSV files, calculates metrics, and plots
voltage/current trends and checkpoint power comparisons over time.

Requirements:
- Python 3.x
- pandas
- matplotlib

Install dependencies:
pip install pandas matplotlib

Usage:
python analysis.py path/to/ix_t_sensor_log.csv
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

def analyze_log(logfile):
    df = pd.read_csv(logfile, parse_dates=['timestamp'])
    df.set_index('timestamp', inplace=True)

    # Calculate power per checkpoint: P = V_bus * I (convert mA to A)
    num_checkpoints = len([col for col in df.columns if 'bus_V' in col])
    power_cols = []
    for i in range(1, num_checkpoints + 1):
        v_col = f'checkpoint_{i}_bus_V'
        i_col = f'checkpoint_{i}_current_mA'
        p_col = f'checkpoint_{i}_power_mW'
        df[p_col] = df[v_col] * (df[i_col] / 1000) * 1000  # power in mW
        power_cols.append(p_col)

    print("Power columns calculated:", power_cols)

    # Plot voltages per checkpoint
    plt.figure(figsize=(12, 6))
    for i in range(1, num_checkpoints + 1):
        plt.plot(df.index, df[f'checkpoint_{i}_bus_V'], label=f'Checkpoint {i} Voltage (V)')
    plt.xlabel('Time')
    plt.ylabel('Bus Voltage (V)')
    plt.title('Checkpoint Bus Voltage Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig('checkpoint_voltage_plot.png')
    plt.show()

    # Plot power per checkpoint
    plt.figure(figsize=(12, 6))
    for p_col in power_cols:
        plt.plot(df.index, df[p_col], label=p_col.replace('_', ' ').title())
    plt.xlabel('Time')
    plt.ylabel('Power (mW)')
    plt.title('Checkpoint Power Over Time')
    plt.legend()
    plt.tight_layout()
    plt.savefig('checkpoint_power_plot.png')
    plt.show()

    # Print summary stats for power columns
    print("\nPower Summary Statistics (mW):")
    print(df[power_cols].describe())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analysis.py path/to/ix_t_sensor_log.csv")
        sys.exit(1)
    analyze_log(sys.argv[1])
