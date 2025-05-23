"""
IX-T Simulation Runner

Simulates the closed-loop energy harvesting and checkpoint recharge
cycles, collecting detailed metrics to validate system feasibility.

Author: [Bryce Wooster]
Version: 1.0.0
"""

import logging
import time
from hardware.interface_code import EnergyHarvesterInterface

class IXTSimulation:
    def __init__(self, cycles=1000, delay=0.05):
        self.cycles = cycles
        self.delay = delay
        self.harvester = EnergyHarvesterInterface()
        self.total_energy_captured = 0.0
        self.energy_log = []

    def run_cycle(self, cycle_num):
        energy = self.harvester.checkpoint_charge()
        self.total_energy_captured += energy
        self.energy_log.append((cycle_num, energy, self.total_energy_captured))
        logging.info(f"Cycle {cycle_num}: Captured Energy = {energy:.3f} V, Total = {self.total_energy_captured:.3f} V")

    def run(self):
        logging.basicConfig(filename='simulation.log', level=logging.INFO,
                            format='%(asctime)s %(message)s')
        print(f"Starting IX-T Simulation for {self.cycles} cycles...")
        for cycle in range(1, self.cycles + 1):
            self.run_cycle(cycle)
            time.sleep(self.delay)
        print("Simulation complete.")
        self.generate_report()

    def generate_report(self):
        avg_energy = self.total_energy_captured / self.cycles
        max_energy = max(e[1] for e in self.energy_log)
        min_energy = min(e[1] for e in self.energy_log)
        print(f"--- Simulation Report ---")
        print(f"Total Cycles Run: {self.cycles}")
        print(f"Total Energy Captured: {self.total_energy_captured:.3f} V")
        print(f"Average Energy per Cycle: {avg_energy:.3f} V")
        print(f"Max Energy in a Cycle: {max_energy:.3f} V")
        print(f"Min Energy in a Cycle: {min_energy:.3f} V")

if __name__ == "__main__":
    sim = IXTSimulation(cycles=500, delay=0.01)
    sim.run()
