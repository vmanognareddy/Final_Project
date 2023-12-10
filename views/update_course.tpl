<!DOCTYPE html>
<html>
<head>
    <title>Edit Course</title>
</head>
<body>
    <h1>Edit Course</h1>
    <form action="/courses/edit/{{course[0]}}" method="post">
        Course Name: <input type="text" name="course_name" value="{{course[1]}}" required>
        <input type="submit" value="Save Changes">
    </form>
    <p><a href="/courses">Back to Courses</a></p>
</body>
</html>
