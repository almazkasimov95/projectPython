# utils/config_loader.py
import yaml
from pathlib import Path


def load_config(env: str = None):
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    env = env or config["default_env"]
    return config["environments"][env]