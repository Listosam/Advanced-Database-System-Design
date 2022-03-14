from bottle import route, run, template

@route('/hello')
#define a function called hello
def hello():
    return "Hello World!"


@route('/')
@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

run(host='localhost', port=8080)