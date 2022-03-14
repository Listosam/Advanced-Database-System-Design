import bottle
from bottle import route, run, template, get, post, request,response, redirect
import dataset
import database

db = dataset.connect('sqlite:///shopping_list.db')

@route('/') #index route
@route('/list')
def get_list():

    shopping_list = database.get_shopping_list()
    return bottle.template('shopping_list', shopping_list=shopping_list, template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/04-Web-using-dataset/Views'])

    

@get('/add')
def get_add():
    return bottle.template('add_item', template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/04-Web-using-dataset/Views'])

@route('/delete/<id>')
def get_delete(id):
    database.delete_item(id)
    #db['list'].delete(id=id)
    redirect('/')
    
#@get('/add')
#def get_add():
  #  return bottle.template('add_item', template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/02-Web-Programming/Views'])

@post('/add')
def post_add():

     description = request.forms.get('description')
     print(f'post was called. description={description}')
     
     
     #table = db['table']
     item = {'description':description}
     database.add_item({'description':description})
     #table.insert(item)
     redirect('/')

@route('/edit/<id>')
def get_edit(id):
     items = [dict(item) for item in db['list'].find(id = id)]
     if len(items) !=1:
         redirect('/')
     items = items[0]
     return bottle.template('edit_item', id=items['id'], description=items['description'], template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/04-Web-using-dataset/Views'])


@post('/edit/<id>')
def post_edit(id):
    description = request.forms.get('description')
    database.update_item(id, description)
    #db['list'].update({'id':id, 'description':description}, ['id'])
    redirect('/list')
    



run(host='localhost', port=8080)