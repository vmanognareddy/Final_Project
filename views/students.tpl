<!DOCTYPE html>
<html>
<head>
    <title>Students</title>
</head>
<body>
    <h1>Students</h1>

    <form action="/students" method="get">
        Search: <input type="text" name="search" value="{{search_term}}">
        <input type="submit" value="Search">
    </form>

    <hr></hr>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Student Name</th>
            <th>Email</th>
            <th>Courses Enrolled</th>
            <th>Update Here</th>
            <th>Delete Here</th>
        </tr>
        % for item in university:
            <tr>
                <td>{{str(item['student_id'])}}</td>
                <td>{{str(item['student_name'])}}</td>
                <td>{{str(item['email'])}}</td>
                <td><a href="/student_courses/{{str(item['student_id'])}}">View Courses</a></td>
                <td><a href="/students/update/{{str(item['student_id'])}}">update</a></td>
                <td><a href="/students/delete/{{str(item['student_id'])}}">delete</a></td>

            </tr>
        % end
    </table>
    <hr/>
<a href="students/add">Add new Student</a>
<hr/>
</body>
</html>
