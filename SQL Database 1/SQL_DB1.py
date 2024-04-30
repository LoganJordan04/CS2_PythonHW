import sqlite3

# Create an SQL School database.
conn = sqlite3.connect("School.db")
c = conn.cursor()

# Create a table in School database for students.
try:
    c.execute("""CREATE TABLE IF NOT EXISTS students
                (student_id INTEGER PRIMARY KEY, last_name TEXT, first_name TEXT, street TEXT, city TEXT, state TEXT,
                zip INTEGER)""")
except:
    pass

# Insert data in students table.
c.execute("INSERT INTO students VALUES (1, 'Smith', 'John', '123 Main St', 'Springfield', 'IL', 62701)")
c.execute("INSERT INTO students VALUES (2, 'Jones', 'Jane', '456 Elm St', 'Chicago', 'IL', 60601)")
c.execute("INSERT INTO students VALUES (3, 'Johnson', 'Jill', '789 Oak St', 'Peoria', 'IL', 61601)")
conn.commit()
