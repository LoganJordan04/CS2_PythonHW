# Logan Jordan SQLite3 Music Database.
import sqlite3


def main():
    # Create an SQL Music database.
    con = sqlite3.connect("Music.db")
    c = con.cursor()

    # Create a table in Music database for Artists.
    c.execute("CREATE TABLE IF NOT EXISTS Artists "
              "(artist_id INTEGER PRIMARY KEY, artist TEXT, genre TEXT, number_recordings INTEGER)")

    # Insert data in Artists table.
    c.execute("INSERT OR REPLACE INTO Artists VALUES (1, 'Miley', 'Rock', 14)")
    c.execute("INSERT OR REPLACE INTO Artists VALUES (2, 'Dolly', 'Country', 123)")
    c.execute("INSERT OR REPLACE INTO Artists VALUES (3, 'Eminem', 'HipHop', 98)")
    c.execute("INSERT OR REPLACE INTO Artists VALUES (4, 'Brittany', 'Rock', 37)")
    con.commit()

    # Create a table in Music database for Genres.
    c.execute("CREATE TABLE IF NOT EXISTS Genres "
              "(genre_id INTEGER PRIMARY KEY, genre TEXT, city TEXT)")

    # Insert data in Genres table.
    c.execute("INSERT OR REPLACE INTO Genres VALUES (1, 'Rock', 'Los Angeles')")
    c.execute("INSERT OR REPLACE INTO Genres VALUES (2, 'Hippie', 'Eugene')")
    c.execute("INSERT OR REPLACE INTO Genres VALUES (3, 'Opera', 'Florence')")
    con.commit()

    # Create a table in Music database for Cities.
    c.execute("CREATE TABLE IF NOT EXISTS Cities "
              "(city_id INTEGER PRIMARY KEY, city TEXT, state TEXT, zip INTEGER, population INTEGER)")

    # Insert data in Cities table.
    c.execute("INSERT OR REPLACE INTO Cities VALUES (1, 'Los Angeles', 'CA', 90001, 18422600)")
    c.execute("INSERT OR REPLACE INTO Cities VALUES (2, 'Eugene', 'OR', 97401, 178000)")
    c.execute("INSERT OR REPLACE INTO Cities VALUES (3, 'Nashville', 'TN', 37011, 1333000)")
    con.commit()

    # Print the Artists rows.
    print("Music Artists")
    for row in c.execute("SELECT * FROM Artists"):
        print(row)

    # Print the Genres rows.
    print("Genres")
    for row in c.execute("SELECT * FROM Genres"):
        print(row)

    # Print the Cities rows.
    print("Cities")
    for row in c.execute("SELECT * FROM Cities"):
        print(row)

    # # Inner join Artists and Genres.
    # for row in c.execute("SELECT artist FROM Artists INNER JOIN Genres ON Artists.genre = Genres.genre"):
    #     print(row)

    # Artist query from user input.
    # Checking the input to see if it matches an artist in the table.
    while True:
        artist_input = input("\nWhich Artist would you like to know more about?: ").lower()
        c.execute(f"SELECT * FROM Artists WHERE LOWER(artist) = '{artist_input}'")
        # If the artist is found then get all needed info from DB.
        if c.fetchall():
            # Fetch the artist from Artists.
            c.execute(f"SELECT artist FROM Artists WHERE LOWER(artist) = '{artist_input}'")
            artist = "".join(map(str, c.fetchone()))

            # Fetch the genre from Artists.
            c.execute(f"SELECT genre FROM Artists WHERE artist = '{artist}'")
            genre = "".join(map(str, c.fetchone()))

            # Fetch the number_recordings from Artists.
            c.execute(f"SELECT number_recordings FROM Artists WHERE artist = '{artist}'")
            num_recordings = "".join(map(str, c.fetchone()))

            # Check if genre is in Genres table.
            c.execute(f"SELECT * FROM Genres WHERE genre = '{genre}'")
            # If the genre is found then get all needed info from DB.
            if c.fetchall():
                # Fetch the city from Genres.
                c.execute(f"SELECT city FROM Genres WHERE genre = '{genre}'")
                city = "".join(map(str, c.fetchone()))

                # Fetch the population from Cities.
                c.execute(f"SELECT population FROM Cities WHERE city = '{city}'")
                population = "".join(map(str, c.fetchone()))

                print(f"{genre} artist {artist} has {num_recordings} recordings and is most popular in {city} "
                      f"with a population of {population}.")

            # If the genre isn't in Genres.
            else:
                print(f"{genre} artist {artist} has {num_recordings} recordings and is popular everywhere.")

            break

        # If the input isn't found.
        else:
            print("Hmm I don't know that one!")

    # Closing the connection.
    con.close()


if __name__ == "__main__":
    main()
