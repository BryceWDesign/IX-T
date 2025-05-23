# /tests/test_checkpoints.py

import unittest
from src.loop import EnergyLoop
from src.checkpoints import CheckpointManager

class TestCheckpointManager(unittest.TestCase):
    def setUp(self):
        self.loop = EnergyLoop(initial_energy=50.0, loss_factor=0.0)
        self.config = [
            {"id": 1, "boost": 30.0},
            {"id": 2, "boost": 25.0}
        ]
        self.manager = CheckpointManager(self.config)

    def test_energize_adds_energy(self):
        self.loop.energy = 10.0
        self.manager.energize(self.loop)
        self.assertEqual(self.loop.energy, 50.0)  # Max energy cap applies

    def test_no_overflow(self):
        self.loop.energy = 49.0
        self.manager.energize(self.loop)
        self.assertEqual(self.loop.energy, 50.0)  # Should not exceed max_energy

if __name__ == "__main__":
    unittest.main()
