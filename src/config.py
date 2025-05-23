# /src/config.py

import json

def load_config(filepath: str) -> dict:
    try:
        with open(filepath, "r") as f:
            config = json.load(f)
        print(f"[CONFIG] Loaded parameters from {filepath}")
        return config
    except Exception as e:
        print(f"[ERROR] Failed to load config: {e}")
        raise
