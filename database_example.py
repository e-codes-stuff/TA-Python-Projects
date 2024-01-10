import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to a SQLite database"""
    try:
        # Create or connect to database
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)


def create_table(c):
    """Create a table in a database using a CREATE TABLE statement"""
    sql_create_table = """
        CREATE TABLE IF NOT EXISTS roster (
            id integer PRIMARY KEY,
            name text NOT NULL,
            species text NOT NULL,
            age integer NOT NULL
        );
        """
    c.execute(sql_create_table)


if __name__ == "__main__":
    # Create the database connection in memory with ":memory:" and create a cursor
    db = create_connection(":memory:")
    c = db.cursor()

    # Create the roster table
    create_table(c)

    # Create list of values to be inserted
    values = [
        ("Jean-Baptiste Zorg", "Human", 50),
        ("Korben Dallas", "Meat Popsicle", 45),
        ("Ak'not", "Elf", 39),
    ]

    # Insert the values into the "roster" table
    c.executemany("INSERT INTO roster (name, species, age) VALUES (?, ?, ?)", values)

    # Set species to Human for Korben Dallas
    c.execute(
        """
            UPDATE roster
            SET species = 'Human' 
            WHERE name = 'Korben Dallas'
        """
    )

    # Select all data for "Human" entries
    c.execute(
        """
        SELECT name, age FROM roster WHERE species = 'Human'
    """
    )

    print("Humans: ")
    for name, age in c.fetchall():
        print("\tName: {}, Age: {}".format(name, age))
