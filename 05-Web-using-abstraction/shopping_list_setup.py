#import dataset

import database
database.setup_shopping_list()
print('Done!')

#db = dataset.connect('sqlite:///shopping_list.db')
#try:

    #db.begin()
    #db['list'].drop()
    #table = db['list']
#
#
    #items = [
    #{'description':'Apples', 'quantity':12, 'variety':'golden delicious'},
    #{'description':'broccoli', 'quantity':4},
    #{'description':'pizza', 'quantity':1, 'toppings':'cheese, peperoni'}, 
    #{'description':'tangerine', 'quantity':6},
    #{'description':'potatoes', 'quantity':3},
    #]

#for item in items:
#    table.insert(item)

#alternative way of inserting items in table
    #table.insert_many(items)
    #db.commit()

#except Exception as e:
    #db.rollback()

