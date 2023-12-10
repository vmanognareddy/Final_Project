<!DOCTYPE html>
<html>
<head>
    <title>Add Course</title>
</head>
<body>
    <h1>Add Course</h1>
    <form action="/student_courses/add" method="post">
        Course Name: <input type="text" name="course_name" required>
        <input type="hidden" name="student_id" value="{{ student_id }}">
        <input type="submit" value="Add Course">
    </form>
    <p><a href="/student_courses">Back to Courses</a></p>
</body>
</html>
