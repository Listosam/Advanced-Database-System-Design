import sqlite3

# create a database called shopping_list
connection = sqlite3.connect('shopping_list.db')
cursor = connection.cursor()
# create a table called list in shopping_list database
cursor.execute("create table list (id integer primary key, description text)")
#Populate the table called list with records
cursor.execute("insert into list (description) values ('Apples')")
cursor.execute("insert into list (description) values ('Bananas')")
cursor.execute("insert into list (description) values ('Tangerines')")
cursor.execute("insert into list (description) values ('Oranges')")
cursor.execute("insert into list (description) values ('Pineapples')")
cursor.execute("insert into list (description) values ('Potatoes')")

#ensure the recorda are committed to the database
connection.commit()
connection.close()
print('Done!')