import sqlite3
import os

def initialize_sqlite_db():
    # Path to the database and SQL script
    db_path = "data/charts.db"
    sql_script_path = "data/sample_data.sql"

    # Ensure the data directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Connect to the SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read the SQL script
    with open(sql_script_path, 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute the SQL script (handles multiple statements)
    cursor.executescript(sql_script)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"SQLite database initialized at {db_path}")

if __name__ == "__main__":
    initialize_sqlite_db()