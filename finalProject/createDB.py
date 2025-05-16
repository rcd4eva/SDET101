import sys
import sqlite3

# Database filename
DB_NAME = "sdet101_test.db"

# Definitions for table schemas: field name -> SQL definition
TABLE_SCHEMAS = {
    "projects": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "notes": "TEXT"
    },
    "fixtures": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "notes": "TEXT"
    },
    "eut_types": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "notes": "TEXT"
    },
    "eut_names": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "notes": "TEXT"
    },
    "status_descr": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "notes": "TEXT"
    },
    "op_descr": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT NOT NULL",
        "notes": "TEXT"
    },
    "endurance_data": {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "date": "TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))",
        "fixture": "INTEGER NOT NULL",
        "project": "INTEGER",
        "eut_type": "INTEGER NOT NULL",
        "eut_name": "INTEGER",
        "op_nbr": "INTEGER NOT NULL",
        "op_dir": "INTEGER",
        "s1_state": "INTEGER",
        "s2_state": "INTEGER",
        "hh": "REAL",
        "icoil": "REAL",
        "vsrc": "REAL",
        "status": "INTEGER NOT NULL",
        "FOREIGN KEY(fixture)": "REFERENCES fixtures(id)",
        "FOREIGN KEY(project)": "REFERENCES projects(id)",
        "FOREIGN KEY(eut_type)": "REFERENCES eut_types(id)",
        "FOREIGN KEY(eut_name)": "REFERENCES eut_names(id)",
        "FOREIGN KEY(s1_state)": "REFERENCES status_descr(id)",
        "FOREIGN KEY(s2_state)": "REFERENCES status_descr(id)",
        "FOREIGN KEY(op_dir)": "REFERENCES op_descr(id)",
        "FOREIGN KEY(status)": "REFERENCES status_descr(id)"
    }
}

def create_table(cursor: sqlite3.Cursor, table_name: str, schema: dict) -> None:
    # Construct and execute a CREATE TABLE statement for `table_name` using `schema`.
    # :param cursor: SQLite database cursor
    # :param table_name: Name of the table to create
    # :param schema: Mapping of column names to SQL definitions
    # :raises sqlite3.Error: if table creation fails
    # Build the column definitions
    columns_sql = ", ".join(
        f"{col} {definition}" for col, definition in schema.items()
    )
    sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql});"
    print(f"Executing SQL for {table_name}:\n{sql}\n")
    cursor.execute(sql)

# Connect to the SQLite database and create all tables defined in TABLE_SCHEMAS.
# :param db_name: Filename of the SQLite database
try:
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    print(f"Connected to {DB_NAME}")
except sqlite3.Error as err:
    print(f"Error connecting to database: {err}")
    sys.exit(1)

# Create each table in the schemas
for table, schema in TABLE_SCHEMAS.items():
    try:
        create_table(cursor, table, schema)
    except sqlite3.Error as err:
        print(f"Error creating table {table}: {err}")
        connection.rollback()
        cursor.close()
        connection.close()
        sys.exit(1)

# Commit changes and clean up
connection.commit()
cursor.close()
connection.close()
print("All tables created successfully.")


