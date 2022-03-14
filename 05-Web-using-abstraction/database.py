import bottle
import dataset

db = dataset.connect('sqlite:///shopping_list.db')

def setup_shopping_list():
    try:

        db.begin()
        db['list'].drop()
        table = db['list']
    
    
        items = [
        {'description':'Apples', 'quantity':12, 'variety':'golden delicious'},
        {'description':'broccoli', 'quantity':4},
        {'description':'pizza', 'quantity':1, 'toppings':'cheese, peperoni'}, 
        {'description':'tangerine', 'quantity':6},
        {'description':'potatoes', 'quantity':3},
        ]

    #for item in items:
    #    table.insert(item)
    
    #alternative way of inserting items in table
        table.insert_many(items)
        db.commit()

    except Exception as e:
        db.rollback()

def get_shopping_list():
    
    items = [dict(item) for item in db['list'].find()]
   
    shopping_list = [{'id':item['id'], 'desc':item['description']} for item in items]
    return shopping_list

    #return bottle.template('shopping_list', shopping_list=shopping_list, template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/04-Web-using-dataset/Views'])

def add_item(item):
    #pass
    db['list'].insert({'description':item})


def delete_item():
    #pass
    db['list'].delete(id=id)

def update_item(id, description):
    db['list'].update({'id':id, 'description':description}, ['id'])
    #pass