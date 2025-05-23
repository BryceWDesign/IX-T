# /src/loop.py

class EnergyLoop:
    def __init__(self, initial_energy: float, loss_factor: float):
        self.energy = initial_energy
        self.loss_factor = loss_factor
        self.max_energy = initial_energy  # Can be extended later

    def advance(self):
        decay = self.energy * self.loss_factor
        self.energy -= decay
        if self.energy < 0:
            self.energy = 0
        print(f"  🔄 Energy loop advanced. Decayed by {decay:.4f} units.")

    def report(self):
        print(f"  📊 Current energy level: {self.energy:.4f} units")
