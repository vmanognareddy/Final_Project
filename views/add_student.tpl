<!DOCTYPE html>
<html>
<head>
    <title>Add Student</title>
</head>
<body>
    <h1>Add Student</h1>
    <form action="/students/add" method="post">
        Student Name: <input type="text" name="student_name" required>
        Email: <input type="email" name="email" required>
        <input type="submit" value="Add Student">
    </form>

    <hr/>
    <a href="/courses/add">Add New Course</a>
    <hr/>


    <p><a href="/students">Back to Students</a></p>
</body>
</html>
