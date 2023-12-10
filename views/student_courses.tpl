<!DOCTYPE html>
<html>
<head>
    <title>Student Courses</title>
</head>
<body>
    <h1>Courses for Student ID {{student_id}}</h1>
    <ul>
        % for item in courses:
            <tr>
            <td>{{str(item['course_id'])}}</td>
            <td>{{str(item['course_name'])}}</td>
            </tr>
        % end
    </ul>

    <hr/>
    <a href="/student_courses/add">Add New Course</a>
    <hr/>
    
    <p><a href="/students">Back to Students</a></p>
</body>
</html>
