
from select import select
import sqlalchemy as db
from sqlalchemy import create_engine, null, true
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy import insert
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import DateTime
from datetime import datetime

engine = create_engine('sqlite:///D:\\SKUL\\Kent State University\\Semester 1\\Advanced Database systems\\Database Code\\Advanced-Database-System-Design\\Courses.db')

#establishes database connection
connection = engine.connect()

#provide more information about Tables
metadata = MetaData()

metadata.create_all(engine)

#Create a table called courses
Courses = Table('Courses', metadata,
      Column('Course_ID', Integer(), primary_key=True),
      Column('Course_Title', String(255), index=True),
      Column('Instructor', String(255)),
      Column('Room_Number', String(50)),
      Column('Credit_Hours', Integer()),
)

#inseert multiple records into Courses table

course_list = [
                { 
                  'Course_Title':'Advanced Database',
                  'Instructor':'Prof. Delozier Gregory',
                  'Room_Number':'Online',
                  'Credit_Hours':3
                },
                { 
                  'Course_Title':'Computer Network Security',
                  'Instructor':'Dr. Maha Allouzi',
                  'Room_Number':'Online',
                  'Credit_Hours':'3'
                },
                { 
                  'Course_Title':'Doctoral Seminar',
                  'Instructor':'Prof. Ruoming Jin',
                  'Room_Number':'MSB 162',
                  'Credit_Hours':'3'
                }
]

student_list = [
                { 
                  
                  'First_Name':'Caswell',
                  'Last_Name':'Eshun',
                  'Study_Level':'Graduate',
                  'Degree_studying':'Masters'
                },
                { 
                    'First_Name':'Felix',
                    'Last_Name':'Ashong',
                    'Study_Level':'Graduate',
                    'Degree_studying':'Doctor of Philosophy'
                },
                { 
                    'First_Name':'Treshanna',
                    'Last_Name':'Stidman',
                    'Study_Level':'Graduate',
                    'Degree_studying':'Masters'
                },
                { 
                    'First_Name':'Gideon',
                    'Last_Name':'Sodipo',
                    'Study_Level':'Graduate',
                    'Degree_studying':'Masters'
                }
]
#insert data into the courses table
ins1 = Courses.insert().values(
    Course_Title  = 'Internet of Things',
    Instructor = 'Gokarna Sharma',
    Room_Number = 'MSB 115',
    Credit_Hours = 3
)

#Create a table called registered students
Registered_Students = db.Table('Registered_Students', metadata,
                  db.Column('student_ID', Integer(), primary_key=True),
                  db.Column('First_Name', String(255), index=True),
                  db.Column('Last_Name', String(255)),
                  db.Column('Study_Level', String(50)),
                  db.Column('Degree_studying', String(255)),
)

#Code for logging the date and time Tables are updated
#db.Column('created_on', DateTime(), default=datetime.now),
#db.Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)

ins2 = Registered_Students.insert().values(
    First_Name = 'Fred',
    Last_Name =  'Rwanda',
    Study_Level = 'Graduate',
    Degree_studying = 'Masters'
)

#ins2 = insert(Registered_Students).values(
    #First_Name='Sampson',
    #Last_Name='Addae',
    #Study_Level='Graduate',
    #Degree_studying='Doctor of Philosophy'
    #created_on=''
    #updated_on=''
#)

#use str(s) to look at the SQL statement the database will see
#print(str(ins1))
#print(str(ins2))

#executing our insert statement to enter our record into the tables
result = connection.execute(ins1, course_list)
result = connection.execute(ins2, student_list)


#compiling our statement
#ins1.compile().params
#ins2.compile().params

#Query the records in our Course table
s = db.select([Courses])

#we can also write the select statement as below
#query_courses = Courses.select(). In this case, we have to import the SELECT from sqlalchemy
rp = connection.execute(s)
query_result = rp.fetchall()

#For loop to print specific column data from the query
for record in query_result:
    print(record.Instructor)

#print all results from the query
#print(query_result)

#Query the records in our Registered_students table
r = Registered_Students.select()
results = connection.execute(r)
students = results.fetchall()
print(students)

for i in students:
    print(i.Last_Name)
#we can also write the select statement as below
#query_courses = Courses.select(). In this case, we have to import the SELECT from sqlalchemy
rp = connection.execute(s)
query_result = rp.fetchall()

#For loop to print specific column data from the query
#for record in query_result:
    #print(record.Instructor)










