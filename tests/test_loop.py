# /tests/test_loop.py

import unittest
from src.loop import EnergyLoop

class TestEnergyLoop(unittest.TestCase):
    def test_energy_decay(self):
        loop = EnergyLoop(initial_energy=100.0, loss_factor=0.1)
        loop.advance()
        self.assertAlmostEqual(loop.energy, 90.0, places=4)

    def test_energy_never_negative(self):
        loop = EnergyLoop(initial_energy=1.0, loss_factor=1.0)
        loop.advance()
        self.assertEqual(loop.energy, 0.0)

    def test_report_output(self):
        loop = EnergyLoop(initial_energy=100.0, loss_factor=0.0)
        loop.report()  # This prints to console but should not crash

if __name__ == "__main__":
    unittest.main()
