


from pymongo import MongoClient
import pymongo
from datetime import datetime




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

#Exercise 6: MongoDB query to display the first 5 restaurant which is in the borough Bronx
#query_6 = restaurants.find({'borough':'Bronx'})[0:5]
#for result in query_6:
#    print(result)

#Exercise 7: MongoDB query to display the next 5 restaurants after skipping first 5 which are in the borough Bronx
#query_7 = restaurants.find({'borough':'Bronx'})[5:10]
#for result in query_7:
#    print(result)

#Exercise 8: MongoDB query to find the restaurants who achieved a score more than 90
#query_8 = restaurants.find({'grades.score':{'$gt': 90}})
#for result in query_8:
 #   print(result)
#print(restaurants.find({'grades.score':{'$gt': 90}}).count())

#Exercise 9: MongoDB query to find the restaurants that achieved a score, more than 80 but less than 100
#query_9 = restaurants.find({'grades.score':{'$gt': 80,'$lt': 100}})
#for result in query_9:
#    print(result)
#print(restaurants.find({'grades.score':{'$gt': 80,'$lt': 100}}).count())

#Exercise 10: Write a MongoDB query to find the restaurants which locate in latitude value less than -95.754168
#query_10 = restaurants.find({'address.coord.0':{'$lt': -95.754168}})
#for result in query_10:
#    print(result)
#print(restaurants.find({'address.coord.0':{'$lt': -95.754168}}).count())

#Exercise 11: MongoDB query to find the restaurants that do not prepare any cuisine of 'American' and their grade score more than 70 and latitude less than -65.754168
#query_11 = restaurants.find({'$and':[{'cuisine':{'$ne':'American'}},{'grades.score':{'$gt':70}},
#{'address.coord.0':{'$lt':-65.754168}}
#]})
#for result in query_11:
#    print(result)
#print(restaurants.find({'$and': [{'cuisine':{'$ne':'American'}},{'grades.score':{'$gt':70}},{'address.coord':{'$lt':-65.754168}}]}).count())

#Exercise 12: MongoDB query to find the restaurants which do not prepare any cuisine of 'American' and achieved a score more than 70 and located in the longitude less than -65.754168.
#Note : Do this query without using $and operator 
#query_12 = restaurants.find({'cuisine':{'$ne':'American'},'grades.score':{'$gt':70},'address.coord':{'$lt':-65.754168}})
#for result in query_12:
#    print(result)
#print(restaurants.find({'cuisine':{'$ne':'American'},'grades.score':{'$gt':70},'address.coord':{'$lt':-65.754168}}).count())

#Exercise 13: MongoDB query to find the restaurants which do not prepare any cuisine of 'American ' and achieved a grade point 'A' not belongs to the borough Brooklyn. 
# The document must be displayed according to the cuisine in descending order
#query_13 = restaurants.find({'cuisine':{'$ne':'American'},'grades.grade':{'$eq':'A'},'borough':{'$ne':'Brooklyn'}}).sort('cuisine',pymongo.DESCENDING)
#for result in query_13:
#    print(result)

#query_13 = restaurants.find({'$and':[{'cuisine':{'$ne':'American'}},
# {'grades.grade':{'$eq':'A'}},{'borough':{'$ne':'Brooklyn'}}]})
#for result in query_13:
#    print(result)

#Exercise 14: MongoDB query to find the restaurant Id, name, 
# borough and cuisine for those restaurants which contain 'Wil' as first three letters for its name
#query_14 = restaurants.find({'name':{'$regex':'^Wil'}},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_14:
#    print(result)

#Exercise 15: MongoDB query to find the restaurant Id, name, borough and 
#cuisine for those restaurants which contain 'ces' as last three letters for its name
#query_15 = restaurants.find({'name':{'$regex':'ces$'}},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_15:
#    print(result)

#Exercise 16: MongoDB query to find the restaurant Id, name, borough and cuisine for those restaurants 
# which contain 'Reg' as three letters somewhere in its name
#query_16 = restaurants.find({'name':{'$regex':'Reg'}},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_16:
#    print(result)

#Exercise 17:MongoDB query to find the restaurants which belong to the borough Bronx and prepared either American or Chinese dish
#query_17 = restaurants.find({'borough':'Bronx','$or':[{'cuisine':'American'},{'cuisine':'Chinese'}]})
#for result in query_17:
#    print(result)

#Exercise 18: MongoDB query to find the restaurant Id, name, borough and cuisine for those 
# restaurants which belong to the  borough Staten Island or Queens or Bronxor Brooklyn
#query_18 = restaurants.find({'borough':{'$in':['Staten Island','Queens','Bronx','Brooklyn']}},
#{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_18:
 #   print(result)

#Exercise 19: MongoDB query to find the restaurant Id, name, borough and cuisine for 
# those restaurants which are not belonging to the borough Staten Island or Queens or Bronxor Brooklyn
#query_19 = restaurants.find({'borough':{'$nin':['Staten Island','Queens','Bronx','Brooklyn']}},
#{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_19:
#    print(result)

#Exercise 20: MongoDB query to find the restaurant Id, name, borough and cuisine for 
# those restaurants which achieved a score which is not more than 10
#query_20 = restaurants.find({'grades.score':{'$lte':10}},{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_20:
 #   print(result)

#Exercise 21:MongoDB query to find the restaurant Id, name, borough and cuisine for those 
# restaurants which prepared dish except  'American' and 'Chinees' or restaurant's name begins with letter 'Wil'
#query_21 = restaurants.find({'$not':{'$in':{'cuisine':['American','Chinese']},'$or':{'name':{'$regex':'^Wil'}}}},
#{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_21:
#    print(result)

#query_21 = restaurants.find({'$nor':[{'cuisine':{'$in':['American','Chinese']}},{'name':{'$regex':'^Wil'}}]},
#{'restaurant_id':1,'name':1,'borough':1,'cuisine':1})
#for result in query_21:
#    print(result)

#Exercise 22: MongoDB query to find the restaurant Id, name, and grades for those restaurants which achieved a grade of "A" 
# and scored 11 on an ISODate "2014-08-11T00:00:00Z" among many of survey dates..
#query_22 = restaurants.find({'grades.grade':'A','grades.score':11,'grades.date':datetime(2014,8,11,0,0)},{'restaurant_id':1,'name':1,'grades':1})
#for result in query_22:
#    print(result)


#Exercise 23: MongoDB query to find the restaurant Id, name and grades for those restaurants 
# where the 2nd element of grades array contains a  grade of "A" and score 9 on an ISODate "2014-08-11T00:00:00Z"
#query_23 = restaurants.find({'grades.1.grade':'A','grades.1.score':9,'grades.1.date':datetime(2014,8,11,0,0)},{'restaurant_id':1,'name':1,'grades':1})
#for result in query_23:
#    print(result)

#Exercise 24: MongoDB query to find the restaurant Id, name, address and geographical location for those restaurants 
# where 2nd element of coord array contains a value which is more than 42 and upto 52
#query_24 = restaurants.find({'address.coord.1':{'$gt':42,'$lte':52}},{'restaurant_id':1,'name':1,'address':1,'coord':1})
#for result in query_24:
#   print(result)

#Exercise 25: MongoDB query to arrange the name of the restaurants in ascending order along with all the columns
#query_25 = restaurants.find().sort('name',pymongo.ASCENDING)
#for result in query_25:
#    print(result)

#Exercise 26:  MongoDB query to arrange the name of the restaurants in descending along with all the columns
#query_26 = restaurants.find().sort('name',pymongo.DESCENDING)
#for result in query_26:
 #   print(result)

#Exercise 27: MongoDB query to arranged the name of the cuisine in ascending order and for that 
# same cuisine borough should be in descending order
#query_27 = restaurants.find({'cuisine':1, 'borough':1}).sort('cusine',pymongo.ASCENDING, 'borough',pymongo.DESCENDING)
#for result in query_27:
#    print(result)

#Exercise 28: MongoDB query to know whether all the addresses contains the street or not
#query_28 = restaurants.find({'address.street':{'$exists':True}})
#for result in query_28:
#   print(result)

#Exercise 29: MongoDB query which will select all documents in the restaurants collection where the coord field value is Double
#query_29 = restaurants.find({'address.coord':{'$type':1}})
#for result in query_29:
#   print(result)


#Exercise 30: MongoDB query which will select the restaurant Id, name and grades for those restaurants which 
# returns 0 as a remainder after dividing the score by 7
#query_30 = restaurants.find({'grades.score':{'$mod':[7,0]}},{'restaurant_id':1,'name':1,'grades':1})
#for result in query_30:
#   print(result)

#Exercise 31: MongoDB query to find the restaurant name, borough, longitude and attitude and cuisine for those 
# restaurants which contains 'mon' as three letters somewhere in its name
#query_31 = restaurants.find({'name':{'$regex':'mon'}},{'name':1,'address.coord':1,'cuisine':1})
#for result in query_31:
#   print(result)

#Exercise 32: MongoDB query to find the restaurant name, borough, longitude and latitude and cuisine for those restaurants 
# which contain 'Mad' as first three letters of its name
query_32 = restaurants.find({'name':{'$regex':'^Mad'}},{'name':1,'borough':1,'address.coord':1,'cuisine':1})
for result in query_32:
   print(result)

