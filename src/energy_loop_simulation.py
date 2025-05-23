"""
Energy Loop Simulation Module for IX-T Project

Simulates the behavior of the energy loop with checkpoints charging the energy flow.
Includes parameters to vary energy retention and checkpoint efficiency.
"""

import numpy as np
import matplotlib.pyplot as plt

class EnergyLoop:
    def __init__(self, initial_energy=100.0, loss_per_cycle=0.05, checkpoint_gain=0.10, cycles=100):
        """
        Initialize the simulation parameters.
        :param initial_energy: Starting energy units
        :param loss_per_cycle: Fractional energy loss per cycle without checkpoint
        :param checkpoint_gain: Fractional energy gain per checkpoint per cycle
        :param cycles: Number of cycles to simulate
        """
        self.initial_energy = initial_energy
        self.loss_per_cycle = loss_per_cycle
        self.checkpoint_gain = checkpoint_gain
        self.cycles = cycles
        self.energy_history = []

    def run(self):
        energy = self.initial_energy
        for cycle in range(self.cycles):
            # Energy lost naturally
            energy *= (1 - self.loss_per_cycle)
            # Energy gained from 3 checkpoints
            energy += energy * self.checkpoint_gain * 3
            self.energy_history.append(energy)
        return self.energy_history

    def plot(self):
        plt.plot(range(1, self.cycles + 1), self.energy_history)
        plt.title('Energy Loop Simulation Over Cycles')
        plt.xlabel('Cycle Number')
        plt.ylabel('Energy Units')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    sim = EnergyLoop()
    sim.run()
    sim.plot()
