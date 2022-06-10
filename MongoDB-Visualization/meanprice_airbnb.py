import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Reading the data from the csv file
myData = pd.read_csv("D:/Airbnb/listingsAndReviews.csv")
myData_pivot = pd.pivot_table(myData, values=["price","security_deposit","cleaning_fee"],
index="address.country", aggfunc={"price":np.mean,"security_deposit":np.mean,"cleaning_fee":np.mean})

#Creating a bar chart grouped by country
ax = myData_pivot.plot(kind="bar",alpha=1)
plt.title('Avg Price, Security_Deposit and Cleaning_fee for Airbnb Listings by Country Using Python')
plt.xlabel('Country')
plt.ylabel('Amount (According to Country Currency)') 
# Show the plot
plt.show()
