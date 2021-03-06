import sqlite3
from bottle import route, run, debug, template, request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todolist WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows = result, template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/todo/views'])
    return output

@route('/new', method='GET')
def new_item():
    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todolist (task,status) VALUES (?,?)", (new,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task', template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/todo/views'])


@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_task', template_lookup = ['D:/SKUL/Kent State University/Semester 1/Advanced Database systems/Database Code/Advanced-Database-System-Design/todo/views'], old=cur_data, no=no)

debug(True)
run(reloader=True)