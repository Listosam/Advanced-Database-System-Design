from tkinter.messagebox import YES
import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('mongodb+srv://Listosam:Mxtojz20@advanced-database-syste.gbeej.mongodb.net/sample_restaurants?retryWrites=true&w=majority')
db = client.sample_restaurants
restaurants = db.restaurants

#Exercise 1: Write a MongoDB query to display all the documents in the collection restaurants
#query_1 = restaurants.find()
#for result_1 in query_1:
#    print(result_1)

#Exercise 2: MongoDB query to display the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant
#query_2 = restaurants.find({},{'restaurant_id':1, 'name':1,'borough':1,'cuisine':1})
#for result_2 in query_2:
#    print(result_2)

#Exercise 3: MongoDB query to display the fields restaurant_id, name, borough and cuisine, but exclude the field _id for all the documents in the collection restaurant
#query_3 = restaurants.find({},{'_id':0,'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result_3 in query_3:
#    print(result_3)

#Exercise 4:MongoDB query to display the fields restaurant_id, name, borough and zip code, but exclude the field _id for all the documents in the collection restaurant
#query_4 = restaurants.find({},{'_id':0,'restaurant_id':1,'name':1,'borough':1,'address.zipcode':1})
#for result_4 in query_4:
#    print(result_4)

#Exercise 5: MongoDB query to display all the restaurant which is in the borough Bronx
#print(restaurants.find_one({'borough':'bronx'}))
#query_5 = restaurants.find({'borough':'Bronx'})
#for result in query_5:
#    print(result)

#Exercise 6:MongoDB query to display the first 5 restaurant which is in the borough Bronx
query_6 = restaurants.find({'borough':'Bronx'})[0:5]
for result in query_6:
    print(result)