<html>
<head>
<title>Connect to database - By George Skouroupathis</title>
</head>
<form action="" method="post">
Username: <input type="text" name="username" id="username">
<br />
Password: <input type="password" name="password" id="password">
</textarea>
<hr />
<input type="submit" value="Connect" />
</form>
<?php
$dbhost = 'fdb1.agilityhoster.com';
$dbuser = $_POST['username'];
$dbpass = $_POST['password'];

$conn = mysql_connect($dbhost, $dbuser, $dbpass) or 
	die('Error connecting to database.');

$dbname = '97282_users';
mysql_select_db($dbname);

mysql_query("INSERT INTO $dbname (FirstName, LastName, Age) 
VALUES ('Peter', 'Griffin', '35')");

mysql_query("SELECT * FROM $dbname WHERE FirstName = 'Peter'");

mysql_close($conn);
?>
</html>