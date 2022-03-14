import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
row = cursor.execute("select * from Shows")

#Print the resultset of a query
for row in row:
    Title, Director, Year = row
    print(Title, Director, Year)
    print(Title)
    print(Director)
    print(Year)

#Format the resultset of a query
print("My top three movies in the last 2 decades are:\n")
for row in row:
    Title, Director, Year = row
    #print(f"My favourite movies in the last 2 decades are {Title}" )
    print(Title)

print("Done!")





