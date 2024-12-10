import sqlite3
import click 
from flask import g
import os


basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = basedir+'../mealWiz.db'

def initialize_db(db_name: str, schema_file: str = 'schema.sql'):
    """Initialize the SQLite database with schema from schema_file."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    with open(schema_file, 'r') as f:
        schema = f.read()
        cursor.executescript(schema)

    connection.commit()
    connection.close()
    print(f"Database '{db_name}' initialized with schema from '{schema_file}'.")

if __name__ == "__main__":
    initialize_db(DATABASE)
