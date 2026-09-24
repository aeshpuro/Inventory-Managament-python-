from getFileProperties.load_to_db_local_files import load_to_db_local_files
from getFileProperties.print_local_files import print_local_files
from getFileProperties.save_local_files import save_local_files


def pipeline(folder_path=".", json_file="file_inventory.json"):
    """Run each step of the file inventory program."""
    print("Step 1: Saving local files to JSON...")
    save_local_files(folder_path, json_file)

    print("Step 2: Printing the saved file information...")
    print_local_files(json_file)

    print("Step 3: Loading files into the database...")
    load_to_db_local_files(json_file)

    print("Pipeline finished.")


if __name__ == "__main__":
    pipeline()
