import json
import os
from pathlib import Path

def load_to_db_local_files(json_file="file_inventory.json"):
    """Load the saved file information into the local_files table."""
    username = os.getenv("DB_USERNAME", "postgres")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    if not password or not database:
        print("Database loading was skipped. Set DB_PASSWORD and DB_NAME first.")
        return

    try:
        from sqlalchemy import create_engine, text
    except ImportError:
        print("Database loading was skipped. Install sqlalchemy and psycopg2 first.")
        return

    engine = create_engine(
        f"postgresql+psycopg2://{username}:{password}@localhost:5432/{database}"
    )

    with Path(json_file).open("r", encoding="utf-8") as file:
        files = json.load(file)

    with engine.connect() as connection:

        query = text("""
            INSERT INTO local_files
                (file_name, file_path, file_size, created_time, modified_time)
            VALUES
                (:file_name, :file_path, :file_size, :created_time, :modified_time)
        """)

        for file_info in files:
            connection.execute(query, file_info)

        connection.commit()

    print(f"Loaded {len(files)} files into the database.")
