from peewee import *
from datetime import date
#create a database called people
db = SqliteDatabase('people.db')

#create a table called Person
class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

#create a table called Pet
class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets') #column 1 referencing the Person table 
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

#we connect to the database called people
db.connect()

#commit the creating of Person & Pet tables
db.create_tables([Person, Pet])

#insert data into the tables
uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save() # bob is now stored in the database


#inserting data into the table using the create() method
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
herb = Person.create(name = 'Herb', birthday=date(1950, 5, 5))

#updating a record using the save() method
grandma.name = 'Grandma L.'
grandma.save()

#insert data into Pet table using the create() method
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

#delete a record from Pet table using delete_instance() method
herb_mittens.delete_instance()

#retrieving a record from the Person table using select.get() method
grandma = Person.select().where(Person.name == 'Grandma L.').get()

#retrieving names of people in Person table
for person in Person.select():
    print(person.name)

#retreiving names of peole who own cats
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print(pet.name, pet.owner.name)

#sorting names of pet owned by uncle Bob alphabetically
for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print(pet.name)




