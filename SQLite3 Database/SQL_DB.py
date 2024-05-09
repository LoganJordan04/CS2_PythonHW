import sqlite3


def main():
    # Create an SQL Music database.
    con = sqlite3.connect("Music.db")
    c = con.cursor()

    # Create a table in Music database for Music_Artists.
    c.execute("CREATE TABLE IF NOT EXISTS Music_Artists "
              "(artist TEXT PRIMARY KEY, genre TEXT, number_recordings INTEGER)")

    # Insert data in Music_Artists table.
    c.execute("INSERT OR REPLACE INTO Music_Artists VALUES ('Miley', 'Rock', 14)")
    c.execute("INSERT OR REPLACE INTO Music_Artists VALUES ('Dolly', 'Country', 123)")
    c.execute("INSERT OR REPLACE INTO Music_Artists VALUES ('Eminem', 'HipHop', 98)")
    c.execute("INSERT OR REPLACE INTO Music_Artists VALUES ('Brittany', 'Rock', 37)")
    con.commit()

    # Print the Music_Artists rows.
    for row in c.execute("select * from Music_Artists"):
        print(row)
    print()

    # Print the Rock artist rows.
    for row in c.execute("select * from Music_Artists where genre=:r", {'r': "Rock"}):
        print(row)

    # Closing the connection.
    con.close()


if __name__ == "__main__":
    main()
