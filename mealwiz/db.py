import sqlite3 #import of database commands
import click #allows primary app to run run sql command to initialize database structures
from flask import g
import os


basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = basedir+'/mealWiz.db'

def initialize_db(db_name: str, schema_file: str = 'schema.sql'):
    """Initialize the SQLite database with schema from schema_file."""
    # Connect to SQLite database (creates the file if it does not exist)
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Read and execute schema from schema.sql
    with open(schema_file, 'r') as f:
        schema = f.read()
        cursor.executescript(schema)

    # Commit changes and close connection
    connection.commit()
    connection.close()
    print(f"Database '{db_name}' initialized with schema from '{schema_file}'.")

if __name__ == "__main__":
    # Set database name (e.g., 'my_database.db') and initialize
    initialize_db(DATABASE)
