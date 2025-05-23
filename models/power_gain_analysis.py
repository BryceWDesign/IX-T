"""
IX-T Power Gain Analysis Model

Simulates energy decay in a loop circuit and evaluates how much ambient energy must be harvested at each checkpoint to offset losses.

Assumptions:
- Fixed decay rate per cycle
- Harvested energy per checkpoint can be independently set
- 3 checkpoints per loop

Author: IX-T Development
"""

import matplotlib.pyplot as plt

# --- Simulation Parameters ---

initial_energy = 1.0  # Initial unit energy (arbitrary units)
decay_per_cycle = 0.05  # 5% loss per full loop
harvested_energy = [0.02, 0.01, 0.015]  # Harvested at each checkpoint
num_cycles = 100

# --- Model Execution ---

energy = initial_energy
energy_history = [energy]

for cycle in range(num_cycles):
    # Apply decay
    energy *= (1 - decay_per_cycle)
    
    # Apply ambient energy checkpoint boosts
    for boost in harvested_energy:
        energy += boost
    
    energy_history.append(energy)

# --- Visualization ---

plt.figure(figsize=(10, 5))
plt.plot(energy_history, label="Net Energy in Loop")
plt.axhline(y=initial_energy, color='gray', linestyle='--', label="Initial Energy")
plt.title("IX-T Loop Energy Over Time")
plt.xlabel("Cycle")
plt.ylabel("Energy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("loop_energy_plot.png", dpi=150)
plt.show()
