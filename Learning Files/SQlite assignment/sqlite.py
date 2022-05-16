import sqlite3 

connection = sqlite3.connect("databaseassignment.db")

with sqlite3.connect("databaseassignment.db") as connection:
    c = connection.cursor()
    c.executescript("""CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName Text, Age INT);
                    INSERT INTO People VALUES('Ron','Obvious','42');
                    """)
    peopleValues = (('Luigi','Vercotti',43),('Arthur','Belling',28))

    c.executemany("INSERT INTO PEOPLE VALUES(?,?,?)", peopleValues)
connection.close()
