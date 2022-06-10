import pymongo
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

client = pymongo.MongoClient('mongodb+srv://Listosam:Mxtojz20@advanced-database-syste.gbeej.mongodb.net/sample_supplies?retryWrites=true&w=majority')
db = client.sample_supplies
myData = db.sales

query_1 = {"customer.age":{"$gte":35},"customer.satisfaction":{"$gte":3}}
supplies = list(myData.find(query_1).limit(1000))
#price = [result['items']['price'] for result in supplies]
age = [result['customer']['age'] for result in supplies]
satisfaction = [result['customer']['satisfaction'] for result in supplies]

#plotting of graph
plt.clf()
fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')
ax.bar(age, satisfaction)

#ax.set_xlabel("price")
ax.set_xlabel("age")
ax.set_ylabel("Satisfaction")

plt.show()

#pressures = [x['pressure']['value'] for x in l]
#air_temps = [x['airTemperature']['value'] for x in l]
#wind_speeds = [x['wind']['speed']['rate'] for x in l]

#plt.clf()
#fig = plt.figure()
  
#ax = fig.add_subplot(111, projection = '3d')
#ax.scatter(pressures, air_temps, wind_speeds)
  
#ax.set_xlabel("Pressure")
#ax.set_ylabel("Air Temperature")
#ax.set_zlabel("Wind Speed")
  
#plt.show()


#supplies = pd.DataFrame(list(myData.find({}, {"_id":0, "saleDate":1, "customer.gender":1, 
#"customer.age":1, "customer.email":1, "customer.satisfaction":1, "couponUsed":1, "purchaseMethod":1})))
#supplies.plot("purchaseMethod")
#print(supplies.head(5))
# Setting the X and Y labels

#What is the average customer satisfaction rating by store — 
#and is this affected by the method of purchase, 
#whether it’s carried out over the phone, in-store or online?
