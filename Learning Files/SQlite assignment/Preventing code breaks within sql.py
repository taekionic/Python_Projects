import sqlite3

#data input from user
"""firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
personData = (firstName, lastName, age)
"""
peopleValues = (('Ron','Obvious', 42), ('Luigi','Vercotti', 43), ('Arthur','Belling',28))


#execute insert statement for supplied person data
with sqlite3.connect('databaseassignment.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastNAme TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)


    #select all first and last names from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    while True: 
        row = c.fetchone()
        if row is None: 
            break
        print(row)

    """for row in c.fetchall():
        print(row)"""