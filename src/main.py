# /src/main.py

from loop import EnergyLoop
from checkpoints import CheckpointManager
from config import load_config

def main():
    # Load simulation parameters
    config = load_config("data/sample_config.json")

    # Initialize the energy loop and checkpoints
    loop = EnergyLoop(initial_energy=config["initial_energy"], loss_factor=config["loss_factor"])
    checkpoints = CheckpointManager(config["checkpoints"])

    print("[IX-T] Starting ambient energy loop simulation...")
    steps = config["simulation_steps"]

    for step in range(steps):
        print(f"\n[Step {step+1}]")
        loop.advance()
        checkpoints.energize(loop)
        loop.report()

    print("\n[IX-T] Simulation complete.")

if __name__ == "__main__":
    main()
