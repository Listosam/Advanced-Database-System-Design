import sqlite3
con = sqlite3.connect('midterm.db') # CREATE DATABASE
cur = con.cursor()
cur.execute("Create table test(Fname text, Lname test, Age int)")
cur.execute("insert into test values('Sampson','Addae', 34)")
con.commit()
con.close()

