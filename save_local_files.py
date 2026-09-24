import json
import os
from pathlib import Path


def save_local_files(folder_path=".", json_file="file_inventory.json"):
    """Find files in one folder and save their information to a JSON file."""
    folder_path = Path(folder_path).resolve()
    json_path = Path(json_file).resolve()

    files = []

    for root, directories, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = Path(root) / filename

            # Do not add the JSON file that this program creates.
            if file_path.resolve() == json_path:
                continue

            try:
                file_info = {
                    "file_name": filename,
                    "file_path": str(file_path),
                    "file_size": file_path.stat().st_size,
                    "created_time": file_path.stat().st_ctime,
                    "modified_time": file_path.stat().st_mtime
                }

                files.append(file_info)

            except OSError:
                # Some files may not allow their information to be read.
                continue

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(files, file, indent=4)

    print(f"Saved {len(files)} files to {json_path.name}.")
    return files
