"""
Energy Loop Simulation for IX-T Project
---------------------------------------

Simulates energy current flow through checkpoints with recharge effects.

This module models the energy retention and boost provided by checkpoints
to evaluate if the loop sustains or grows energy over time.

Uses basic physics and simplified assumptions to test the concept.
"""

import numpy as np
import matplotlib.pyplot as plt

class EnergyLoopSimulator:
    def __init__(self, initial_energy=100.0, checkpoint_efficiency=1.05, decay_factor=0.98, steps=100):
        """
        initial_energy: starting energy units
        checkpoint_efficiency: multiplier at each checkpoint (>1 means energy boost)
        decay_factor: energy loss per step in the loop (<1 means loss)
        steps: number of simulation steps
        """
        self.energy = initial_energy
        self.checkpoint_efficiency = checkpoint_efficiency
        self.decay_factor = decay_factor
        self.steps = steps
        self.energy_history = []

    def run(self):
        energy = self.energy
        for step in range(self.steps):
            # Pass through three checkpoints per loop
            for _ in range(3):
                energy *= self.checkpoint_efficiency
            # Energy decays after full loop
            energy *= self.decay_factor
            self.energy_history.append(energy)
        return self.energy_history

if __name__ == "__main__":
    sim = EnergyLoopSimulator()
    history = sim.run()
    import matplotlib.pyplot as plt
    plt.plot(history)
    plt.xlabel('Simulation Step')
    plt.ylabel('Energy Units')
    plt.title('Energy Loop Simulation over Time')
    plt.grid(True)
    plt.show()
