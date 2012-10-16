<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>

<meta http-equiv="content-type" content="text/html;charset=utf-8">

<meta name="description" content="AstroCamel was brought to you to provide the internet users the opportunity to share information through the web. Browse code snippets and artwork freely.">

<meta name="keywords" content="torrents, free, free torrents, torrent, music, pictures, movies, apps, applications, astrocamel, www.astrocamel.com, astrocamel.com, astro, camel, astro camel, astro-camel, astrocamel radio, radio, online radio">

<meta name="author" content="George Skouroupathis">
<meta name="revisit-after" content="20 days">
<meta name="ROBOTS" content="Index, ALL">
<meta name="ROBOTS" content="Index, FOLLOW">

<title>Message Center - AstroCamel.com</title>

<link rel="stylesheet" type="text/css" href="style-msg.css?derp=derp" />

<link rel="icon" type="image/x-icon" href="favicon.ico" />
<link rel="shortcut icon" type="image/x-icon" href="favicon.ico" />

</head>
<body onload="document.googleform.q.focus();document.googleform.q.select()">

<br />
<br />
<br />
<br />
<br />

<div id="toprocks">
</div>

<div id="main">
	
	<div id="content">
<center>

<?php

#Define filter_input () to avoid SQL and HTML Injection
function filter_mainput($input){
	return htmlspecialchars(str_replace(";","/;/",$input));
}

$first = filter_mainput($_POST['first_name']);
$last = filter_mainput($_POST['last_name']);
$email = filter_mainput($_POST['email']);
$tel = filter_mainput($_POST['telephone']);
$comments = filter_mainput($_POST['comments']);

$time = time();
$time = $time % 86400;
$hours = intval($time / 3600);
$mins = intval(($time % 3600) / 60);
$hours += 3;#Time zones
if ($hours > 23)
	{
	$hours -= 24;
	}
if (strlen($hours) == 1)
	{
	$hours = "0" + $hours;
	}
$date = date("d/m/Y") . "-" . $hours .":" . $mins;

$user="a2207475_1";
$password="a2207475_2";
$database="a2207475_db";
mysql_pconnect("mysql2.000webhost.com",$user,$password);
@mysql_select_db($database) or die( "Unable to select database");

$query = "INSERT INTO msgs VALUES ('', '$first', '$last', '$email', '$tel', '$comments', '$date')";
if ($first!="" or $last!="" or $email!="" or $tel!="" or $comments!="" and $comments!="Type your message here.")
{
	if (mysql_query($query))
	{
		echo "Message succesfully sent! Click <a href=\"http://www.astrocamel.com/contact.html\">here</a> to go back.";
	}
	else
	{
		echo "Oops! Something went wrong. Click <a href=\"http://www.astrocamel.com/contact.html\">here</a> to try again.";
	}
}
else
{
	echo "Oops! You left all the values blank! Click <a href=\"http://www.astrocamel.com/contact.html\">here</a> to try again.";
}
mysql_close()
?>
</center>

	</div>

	<div id="fix">
	</div>
</div>

<div id="bottomrocks">
</div>

</body>
</html>