"""
IX-T Energy Loop Simulation
Simulates energy current behavior with checkpoints charging mechanism.
"""

import numpy as np
import matplotlib.pyplot as plt

class EnergyLoopSimulator:
    def __init__(self, initial_energy=100.0, loss_factor=0.1, charge_factor=0.15, steps=100):
        """
        initial_energy: starting energy in loop
        loss_factor: percentage of energy lost per step (0 < loss_factor < 1)
        charge_factor: percentage of energy added at checkpoints per step
        steps: total simulation steps
        """
        self.initial_energy = initial_energy
        self.loss_factor = loss_factor
        self.charge_factor = charge_factor
        self.steps = steps
        self.energy_history = []

    def simulate(self):
        energy = self.initial_energy
        checkpoints = [0.0, 0.0, 0.0]  # Energy added at 3 checkpoints each step

        for step in range(self.steps):
            # Energy lost
            energy -= energy * self.loss_factor

            # Energy added by checkpoints
            added_energy = energy * self.charge_factor
            energy += added_energy  # Assume checkpoints add energy proportional to current energy

            self.energy_history.append(energy)

        return self.energy_history

    def plot(self):
        plt.plot(self.energy_history)
        plt.title("Energy Over Time in Simulated Loop")
        plt.xlabel("Step")
        plt.ylabel("Energy")
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    sim = EnergyLoopSimulator()
    sim.simulate()
    sim.plot()
