<!DOCTYPE html>
<html>
<head>
    <title>Update Student</title>
</head>
<body>
    <h1>Update Student</h1>
    <form action="/students/update/{{str(item['student_id'])}}" method="post">
        <input type="hidden" name="student_id" value="{{str(item['student_id'])}}"/>
        Student Name: <input type="text" name="student_name" value="{{str(item['student_name'])}}" required>
        Email: <input type="email" name="email" value="{{str(item['email'])}}" required>
        <input type="submit" value="Save Changes">
    </form>
    <p><a href="/students">Back to Students</a></p>
</body>
</html>
