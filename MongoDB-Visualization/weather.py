# Using PyMongo to create plots
import pymongo
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

	
url = 'mongodb+srv://Listosam:Mxtojz20@advanced-database-syste.gbeej.mongodb.net/sample_supplies?retryWrites=true&w=majority'
client = pymongo.MongoClient(url)

# sample dataset
db = client['sample_weatherdata']

# sample collection
weather_data = db['data']

# remove outliers that are clearly bad data
query = {
	'pressure.value': { '$lt': 9999 },
	'airTemperature.value': { '$lt': 9999 },
	'wind.speed.rate': { '$lt': 500 },
}

# convert our cursor into a list
l = list(weather_data.find(query).limit(1000))

# pull out the 3 variables we care
# about into their own respective lists
pressures = [x['pressure']['value'] for x in l]
air_temps = [x['airTemperature']['value'] for x in l]
wind_speeds = [x['wind']['speed']['rate'] for x in l]

# here you'll write the code to plot pressures,
# air_temps, and wind_speeds in a 3D plot
plt.clf()
fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')
ax.scatter(pressures, air_temps, wind_speeds)

ax.set_xlabel("Pressure")
ax.set_ylabel("Air Temperature")
ax.set_zlabel("Wind Speed")

plt.show()
