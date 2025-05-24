"""
Simulated capacitor charging from ambient RF energy captured by checkpoint antennas.
Model shows viability of low-current, high-frequency ambient charging model.
"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 915e6  # Hz (ISM band, typical RFID)
power_density = 1e-3  # W/m^2 - simulated urban environment
capture_area = 0.01  # m^2 - effective aperture of antenna
efficiency = 0.5     # 50% conversion efficiency
capacitance = 1e-3   # Farads (large supercapacitor)
initial_voltage = 2.5  # V
target_voltage = 5.0  # V
sample_time = 0.1  # s
total_time = 300  # s

# Derived values
received_power = power_density * capture_area * efficiency  # Watts
charge_rate = received_power / target_voltage  # Amps

# Time simulation
timesteps = int(total_time / sample_time)
voltages = [initial_voltage]
times = [0]

for i in range(1, timesteps):
    t = i * sample_time
    current_voltage = voltages[-1]
    if current_voltage >= target_voltage:
        break
    # Using Q = CV, dQ/dt = I => dV = I/C * dt
    dv = (charge_rate / capacitance) * sample_time
    voltages.append(min(current_voltage + dv, target_voltage))
    times.append(t)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(times, voltages, label='Capacitor Voltage')
plt.axhline(y=target_voltage, color='r', linestyle='--', label='Target Voltage')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Simulated RF Ambient Charging of Capacitor")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
