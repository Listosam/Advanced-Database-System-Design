import bottle
from bottle import get, post, request, run, template, route, error


#define a method/function called login
#@get('/login') # or @route('/login')
#def login():
    
 #   return '''
 #        <form action="/login" method="post">
 #           Username: <input name="username" type="text" />
 #           Password: <input name="password" type="password" />
 #           Select a file: <input type="file" name="upload" />
 #           <input value="Login" type="submit" />
 #     </form>
 #  '''

@route('/login') # or @route('/login')
def login_page():
    return template('login', template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/MidTerm-exam-practice/views'])


@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host="localhost", port = 8080)