'''from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    people_names = ['Magik', 'Gideon', 'Creswell']
    return template('<b>Hello! {{name}}</b>', name=people_names)

run(host='localhost', port=8080)'''

from bottle import route, run, template

@route('/hello')
def index():
    people_names = ['Magik', 'Gideon', 'Creswell']
    return template('D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/02-Web-Programming/Views/hello.tpl', name=people_names)

run(host='localhost', port=8080)