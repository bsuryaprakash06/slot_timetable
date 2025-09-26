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
  <title>Time Table: B Surya Prakash</title>
</head>
<body align="center">
  <img src="/static/logo.png" alt="description" width="700" height="100">

  <table border="1" align="center" bgcolor="#f2f2f2">
    <caption><b>Time Table -  B Surya Prakash</b></caption>
    <tr bgcolor="#4CAF50" style="color:white;">
      <th>Day/Time</th>
      <th>8-10</th>
      <th>10-12</th>
      <th>1-3</th>
      <th>3-5</th>
    </tr>
    <tr>
      <th bgcolor="#e0e0e0">Monday</th>
      <td>FREE SLOT</td>
      <td>GER</td>
      <td>FREE SLOT</td>
      <td>FREE SLOT</td>
    </tr>
    <tr bgcolor="#f9f9f9">
      <th>Tuesday</th>
      <td>GER</td>
      <td>FREE SLOT</td>
      <td>MAT</td>
      <td>FREE SLOT</td>
    </tr>
    <tr>
      <th bgcolor="#e0e0e0">Wednesday</th>
      <td>PHY</td>
      <td>FREE SLOT</td>
      <td>FWAD</td>
      <td>GER</td>
    </tr>
    <tr bgcolor="#f9f9f9">
      <th>Thursday</th>
      <td>PHY</td>
      <td>FWAD</td>
      <td>FWAD</td>
      <td>CHE</td>
    </tr>
    <tr>
      <th bgcolor="#e0e0e0">Friday</th>
      <td>CHE</td>
      <td>FWAD</td>
      <td>SS</td>
      <td>GER</td>
    </tr>
  </table>

  <table border="1" align="center" bgcolor="#f2f2f2">
    <caption><b>Subject Codes</b></caption>
    <tr bgcolor="#4CAF50" style="color:white;">
      <th>S. No.</th>
      <th>Subject Code</th>
      <th>Subject Name</th>
    </tr>
    <tr>
      <td>1</td>
      <td>19AI414</td>
      <td>Fundamentals of Web Application Development (FWAD)</td>
    </tr>
    <tr bgcolor="#f9f9f9">
      <td>2</td>
      <td>19EN612</td>
      <td>German Basic (GER)</td>
    </tr>
    <tr>
      <td>3</td>
      <td>19PH206</td>
      <td>Physics for Information Technology (PHY)</td>
    </tr>
    <tr bgcolor="#f9f9f9">
      <td>4</td>
      <td>19CY205</td>
      <td>Principles of Chemistry in Engineering (CHE)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>19MA201</td>
      <td>Calculus and Matrix Algebra (MAT)</td>
    </tr>
    <tr bgcolor="#f9f9f9">
      <td>6</td>
      <td>19ET701</td>
      <td>Soft Skills (SS)</td>
    </tr>
  </table>
</body>
</html>

```

## OUTPUT
<img width="1919" height="1102" alt="image" src="https://github.com/user-attachments/assets/6919bf48-dd95-4575-84a6-93a6266d98a9" />



## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
