<?php
$username = $_POST['username'];
$password = $_POST['password'];

if ($username == "admin" && $password == "enterthecamel" or $_SESSION['authed'] === TRUE) {
	$_SESSION['authed'] = TRUE;
	echo "<center>Welcome, AstroCamel admin.<//center>";
	}
	else {
	echo "<center>Wrong login.<//center>";
	$_SESSION['authed'] = FALSE;
	}

?>