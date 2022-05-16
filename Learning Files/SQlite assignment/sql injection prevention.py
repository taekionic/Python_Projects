import sqlite3

#data input from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

#execute insert statement for supplied person data

with sqlite3.connect('databaseassignment.db') as connection:
    c = connection.cursor()
    line = "INSERT INTO People VALUES ('"+firstName + "', '"+lastName +"', " +str(age) +")"
    c.execute(line)
    print(line)