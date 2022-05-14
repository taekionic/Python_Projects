import sqlite3
import os
from pathlib import Path

def startdb():  #creating a function to create our database and insert our table if it does not already exist
    conn = sqlite3.connect('database2.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS dbassignment ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename varchar(50) \
            )")
        conn.commit()
    conn.close()


def filesearch(): #creating a function to search through our file directory 
    dirname = ('fileList')
    conn = sqlite3.connect('database2.db')
    for files in os.listdir(dirname):
        if files.endswith('txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("\
                    INSERT INTO dbassignment (col_filename) VALUES (?)", (files,))
                print(files)
                
        else:
            continue

startdb()
filesearch()





"""def filesearch():
    dirname = 'C:\\Users\\Cagol\\OneDrive\\Documents\\GitHub\\Python_Projects\\Database\\fileList'
    conn = sqlite3.connect('database2.db')
    for files in os.listdir(dirname):
        if files.endswith('txt'):
            with conn:
                cur = conn.cursor()
                cur.execute("IF NOT EXISTS (SELECT col_filename FROM dbassignment WHERE col_filename=files)\
                    INSERT INTO dbassignment (col_filename) VALUES (?)", (files,))
                print(files)
                
        else:
            continue"""





