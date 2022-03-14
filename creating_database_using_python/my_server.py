from unicodedata import name
'''from bottle import route, run, template
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>', name='Sampson Addae!')
 
run(host='localhost', port=8080)'''

from bottle import route, run, template
@route('/hello/')
def index():
    people_names = ['Magik', 'Gideon', 'Creswell']
    return template('hello.tpl', people=people_names)

run(host='localhost', port=8080)

