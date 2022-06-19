import json
from pathlib import Path



def load_config(configPath: Path) -> dict:
    print(Path.cwd())
    print(f"Path - {configPath}")
    try:
        with open(configPath, "r") as config_file:
            configJson = json.load(config_file)
        return configJson
    except FileNotFoundError as e:
        # print(e)
        return {}
