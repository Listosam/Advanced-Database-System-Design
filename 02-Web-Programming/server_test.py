import bottle
from bottle import route, run, template
import sqlite3

connection = sqlite3.connect('shopping_list.db')
@route('/list')
def get_list():
    global connection
    cursor = connection.cursor()
    items = cursor.execute("select id, description from list")

    items = list(items)
    items = [{'id':item[0], 'desc':item[1]} for item in items]
    #print(items)
    #items = [item[0] for item in items]
    shopping_list = ['Bananas', 'Apples', 'Oranges', 'Cucumbers','Tangerines']
    return bottle.template('shop_list', shopping_list=shopping_list, template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/02-Web-Programming/Views'])


@route('/add')
def get_add():
    return bottle.template('add_item', template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/02-Web-Programming/Views'])




@route('/delete/<id>')
def get_delete(id):
    global connection
    cursor = connection.cursor()
    items = cursor.execute(f'delete from list where id={id}')
    return bottle.template('confirm_delete', id=id, template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/02-Web-Programming/Views'])

run(host='localhost', port=8080)