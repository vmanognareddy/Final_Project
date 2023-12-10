import sqlite3
from bottle import Bottle, route, post, run, template, request, redirect

connection = sqlite3.connect("university.db")

route('/students')
def get_students(student_id=None):
    
    cursor = connection.cursor()
    search_term = request.query.get('search', '').strip()
    if search_term:
       rows = cursor.execute("SELECT * FROM students WHERE student_name LIKE ?", (f"%{search_term}%",))
    # if search_term:
    #     rows = cursor.execute("SELECT student_id, student_name, email from students where student_name LIKE ?", (f"%{search_term}%",))
    else:
        rows = cursor.execute(f"select student_id,student_name, email from students")
    rows = cursor.fetchall()
    rows = [ {'student_id' : row[0], 'student_name': row[1], 'email' : row[2]} for row in rows ]
    # return template('students', rows=rows, search_term=search_term)
    return rows


def get_courses(student_id):
    cursor = connection.cursor()
    # Fetch courses associated with the student
    # cursor.execute("SELECT courses.course_name FROM courses JOIN enrollment ON courses.course_id = enrollment.course_id WHERE enrollment.student_id = ?", (student_id,))
    cursor.execute("SELECT courses.course_id, courses.course_name FROM courses JOIN enrollment ON courses.course_id = enrollment.course_id WHERE enrollment.student_id = ?", (student_id,))
    
    rows = cursor.fetchall()
    rows = [ {'course_id' : row[0], 'course_name': row[1]} for row in rows ]
    return rows
    

def add_students(student_name, email):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO students (student_name, email) VALUES (?, ?)", (student_name, email))
    connection.commit()

def add_course(student_id, course_name):
    cursor = connection.cursor()
    statement = "INSERT INTO courses(student_id, course_name) VALUES (?, ?)"
    cursor.execute(statement, (student_id, course_name))
    connection.commit()


def update_student(student_id, student_name, email):
    cursor = connection.cursor()
    statement = f"update students set student_name='{student_name}', email='{email}' where student_id={student_id}"
    cursor.execute(statement)
    connection.commit()

def delete_item(student_id):
    cursor = connection.cursor()
    cursor.execute(f"delete from students where student_id={student_id}")
    connection.commit()


def set_up_database():
    cursor = connection.cursor()
    try:
        cursor.execute("drop table list")
    except:
        pass

    # Create students table
    cursor.execute('''
    create table IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
    

    # Create courses table
    cursor.execute('''
    create table IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL
    )
''')

# Create enrollment table to represent the many-to-many relationship between students and courses
    cursor.execute('''
    create table IF NOT EXISTS enrollment (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id TEXT NOT NULL, 
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
''')
    


connection.commit()

