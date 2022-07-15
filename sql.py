import sqlite3

# creates a database if it doesn't exist
with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("DROP TABLE posts")
    # creates a table
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")
    # inserting data
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')