import sqlite3
connection = sqlite3.connect('shopping_list.db')
cursor = connection.cursor()
rows = cursor.execute("select id,description from list")


#Print the resultset of a query
rows = list(rows)
#print(rows)
#rows = [row[0] for row in rows]
rows = [{'id':row[0], 'desc':row[1]} for row in rows]
#print(rows)

print("Done!")





