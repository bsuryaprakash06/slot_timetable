# Ex 03 Time Table
## Date: 24-09-2025

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Table of Contents</title>
</head>
<body>
  <center>
  <img src="/static/logo.png" alt="description" width="700" height="100">
  </center>
  <center>
  <table border="1" style="width:80%" height="90%">
    <caption><h1>My TimeTable</h1></caption>
    <tr>
      <th>Time</th>
      <th>8-10</th>
      <th>10-12</th>
      <th>1-3</th>
      <th>3-5</th>
    </tr>
    <tr>
      <th>Monday</th>
      <td>BEEE</td>
      <td>ML</td>
      <td>WEB</td>
      <td>SE</td>
    </tr>
    <tr>
      <th>Tuesday</th>
      <td>Maths</td>
      <td>Adv C</td>
      <td>BEEE</td>
      <td>— No Class —</td>
    </tr>
    <tr>
      <th>Wednesday</th>
      <td>— No Class —</td>
      <td>Web</td>
      <td>— Mentor Meet —</td>
      <td>QA</td>
    </tr>
    <tr>
      <th>Thursday</th>
      <td>ML</td>
      <td>Maths</td>
      <td>HRM</td>
      <td>SE</td>
    </tr>
    <tr>
      <th>Friday</th>
      <td>Adv C</td>
      <td>— No Class —</td>
      <td>HRM</td>
      <td>— No Class —</td>
    </tr>
    </center>
  </table>
</body>
</html>
```

## OUTPUT
<img width="1919" height="1145" alt="Static" src="https://github.com/user-attachments/assets/abc6ecab-be05-4801-b4c9-a215cd0afe85" />


## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
