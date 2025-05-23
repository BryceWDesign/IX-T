# /src/checkpoints.py

class Checkpoint:
    def __init__(self, location_id: int, boost_amount: float):
        self.location_id = location_id
        self.boost_amount = boost_amount

    def apply(self, loop):
        print(f"  ⮕ Checkpoint {self.location_id} boosts energy by {self.boost_amount:.2f}")
        loop.energy += self.boost_amount
        if loop.energy > loop.max_energy:
            loop.energy = loop.max_energy
            print("    ⚠️ Energy capped at system max.")

class CheckpointManager:
    def __init__(self, checkpoint_configs):
        self.checkpoints = [
            Checkpoint(cfg["id"], cfg["boost"]) for cfg in checkpoint_configs
        ]

    def energize(self, loop):
        print("  🔋 Passing through checkpoints...")
        for cp in self.checkpoints:
            cp.apply(loop)
