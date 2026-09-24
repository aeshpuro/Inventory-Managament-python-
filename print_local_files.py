import json
from pathlib import Path


def print_local_files(json_file="file_inventory.json"):
    """Print the saved file information in an easy-to-read format."""
    json_path = Path(json_file)

    if not json_path.exists():
        print("The JSON file was not found.")
        return

    with json_path.open("r", encoding="utf-8") as file:
        files = json.load(file)

    print(json.dumps(files, indent=4))
