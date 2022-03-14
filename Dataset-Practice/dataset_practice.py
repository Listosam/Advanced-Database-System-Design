import dataset
db = dataset.connect('sqlite:///mydatabase.db')
table = db['user']
table.insert(dict(name = 'Sampson Addae', age = 34, country = 'Ghana'))
table.insert(dict(name = 'Sampson Addae', age = 34, country = 'Ghana', gender = 'Male'))
table.update(dict(name= 'Sampson Addae', age=47), ['name'])
table.insert(dict(name = 'Sampson Addae', age = 34, country = 'Ghana'))

db.begin()
try:
    db['user'].insert(dict(name='Felix Akinboyewa', age=46, country='Nigeria'))
    db['user'].insert(dict(name='Caswell Eshun', age=27, country='Ghana'))
    db.commit()
except:
    db.rollback()

users = db['user'].all()

for user in users:
    print(user)
    