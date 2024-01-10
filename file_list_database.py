import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Create a connection to a database
conn = sqlite3.connect('file_list.db')
c = conn.cursor()

# Create a table with an auto-incrementing ID and a string field for filenames
c.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL
    )
''')


# Filtering out files that end with .txt and inserting them into the database
for file in fileList:
    if file.endswith('.txt'):
        c.execute('INSERT INTO files (filename) VALUES (?)', (file,))

conn.commit()

# Query to select all .txt files from the database
c.execute('SELECT filename FROM files')
txt_files = c.fetchall()

print("Text files in the database:")
for file in txt_files:
    print(file[0])

conn.close()
