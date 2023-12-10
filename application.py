from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    return template('index')

@route("/students")
def get_list():
    items = database.get_students()
    search_term = request.forms.get('search_term')
    return template('students', university=items, search_term=search_term)

@route("/student_courses/<student_id:int>")
def get_courses(student_id):
    items = database.get_courses(student_id)
    # student_id = request.forms.get("student_id")
    return template('student_courses', student_id=student_id, courses=items)


# @route("/student_courses/add")
# def get_course_add():
#     student_id = request.forms.get("student_id")
#     return template("add_course.tpl", student_id=student_id)

# @post("/student_courses/add")
# def post_courses():
#     course_name = request.forms.get("course_name")
#     student_id = request.forms.get("student_id")
#     # print("description = ", [description])
#     database.add_course(student_id,course_name)
#     redirect(f"/student_courses/{student_id}")

@route("/student_courses/add", method=['GET', 'POST'])
def post_courses():
    if request.method == 'POST':
        course_name = request.forms.get("course_name")
        student_id = request.forms.get("student_id")
        database.add_course(student_id, course_name)
        redirect(f"/student_courses/{student_id}")
    else:
        student_id = request.query.get("student_id")
        return template('add_course.tpl', student_id=student_id)

@route("/students/add")
def get_add():
    return template("add_student.tpl")

@post("/students/add")
def post_add():
    student_name = request.forms.get("student_name")
    email = request.forms.get("email")
    # print("description = ", [description])
    database.add_students(student_name, email)
    redirect("/students") 
 

@route("/students/update/<student_id>")
def get_update(student_id):
    items = database.get_students(student_id)
    print(items)
    return template("update_student.tpl", item=items[0])

@post("/students/update/<student_id>")
def post_update(student_id):
    student_name = request.forms.get("student_name")
    email = request.forms.get("email")
    student_id = request.forms.get("student_id")
    # id = request.forms.get("id")
    #print("/update",[id,description])
    database.update_student(student_id, student_name, email)
    redirect("/students")    

@route("/students/delete/<student_id>")
def get_delete(student_id):
    database.delete_item(student_id)
    redirect("/students")


run(host='localhost', port=8090)

# from bottle import Bottle, route, post, run, template, request, redirect
# import sqlite3
# import database

# app = Bottle()

# # SQLite Database Initialization
# conn = sqlite3.connect('university.db')
# cursor = conn.cursor()

# # Create students table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS students (
#         student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_name TEXT NOT NULL,
#         email TEXT NOT NULL
#     )
# ''')

# # Create courses table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS courses (
#         course_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course_name TEXT NOT NULL
#     )
# ''')

# # Create enrollment table to represent the many-to-many relationship between students and courses
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS enrollment (
#         enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_id INTEGER,
#         course_id INTEGER,
#         FOREIGN KEY (student_id) REFERENCES students(student_id),
#         FOREIGN KEY (course_id) REFERENCES courses(course_id)
#     )
# ''')

# conn.commit()

# # Routes

# @app.route('/')
# def index():
#     return template('index')

# # Students CRUD

# @app.route('/students')
# def students():
#     search_term = request.query.get('search', '').strip()

#     # Fetch students based on search_term
#     if search_term:
#         cursor.execute("select * from students where student_name LIKE ?", (f"%{search_term}%",))
#     else:
#         cursor.execute("select * from students")

#     result = cursor.fetchall()

#     return template('students', rows=result, search_term=search_term)

# @app.route('/student_courses/<student_id:int>')
# def student_courses(student_id):
#     # Fetch courses associated with the student
#     cursor.execute("select courses.course_name from courses JOIN enrollment ON courses.course_id = enrollment.course_id whhere enrollment.student_id = ?", (student_id,))
#     result = cursor.fetchall()

#     return template('student_courses', student_id=student_id, courses=result)


# @app.route('/students/add', method='GET')
# def add_student_form():
#     return template('add_student')

# @app.route('/students/add', method='POST')
# def add_student():
#     student_name = request.forms.get('student_name')
#     email = request.forms.get('email')

#     cursor.execute("insert into students (student_name, email) values (?, ?)", (student_name, email))
#     conn.commit()

#     redirect('/students')

# @app.route('/students/edit/<student_id:int>', method='GET')
# def edit_student_form(student_id):
#     cursor.execute("select * from students where student_id=?", (student_id,))
#     student = cursor.fetchone()
#     return template('edit_student', student=student)

# @app.route('/students/edit/<student_id:int>', method='POST')
# def edit_student(student_id):
#     student_name = request.forms.get('student_name')
#     email = request.forms.get('email')

#     cursor.execute("update students SET student_name=?, email=? where student_id=?", (student_name, email, student_id))
#     conn.commit()

#     redirect('/students')

# @app.route('/students/delete/<student_id:int>')
# def delete_student(student_id):
#     cursor.execute("delete from students where student_id=?", (student_id,))
#     conn.commit()

#     redirect('/students')

# # Courses CRUD

# @app.route('/courses')
# def courses():
#     cursor.execute("select * from courses")
#     result = cursor.fetchall()
#     return template('courses', rows=result)

# @app.route('/courses/add', method='GET')
# def add_course_form():
#     return template('add_course')

# @app.route('/courses/add', method='POST')
# def add_course():
#     course_name = request.forms.get('course_name')

#     cursor.execute("insert into courses (course_name) VALUES (?)", (course_name,))
#     conn.commit()

#     redirect('/courses')

# @app.route('/courses/edit/<course_id:int>', method='GET')
# def edit_course_form(course_id):
#     cursor.execute("select * from courses where course_id=?", (course_id,))
#     course = cursor.fetchone()
#     return template('edit_course', course=course)

# @app.route('/courses/edit/<course_id:int>', method='POST')
# def edit_course(course_id):
#     course_name = request.forms.get('course_name')

#     cursor.execute("update courses SET course_name=? where course_id=?", (course_name, course_id))
#     conn.commit()

#     redirect('/courses')

# @app.route('/courses/delete/<course_id:int>')
# def delete_course(course_id):
#     cursor.execute("delete from courses where course_id=?", (course_id,))
#     conn.commit()

#     redirect('/courses')

# # Static Routes
# @app.route('/static/<filename:path>')
# def static(filename):
#     return bottle.static_file(filename, root='./static')

# Run the application
# if __name__ == '__main__':
#     run(app, host='localhost', port=8090, debug=True)
