<?php

$pass=$_POST['pass'];

if ($pass!="123") header('Location: http://www.astrocamel.com') ;

?>
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

<title>AstroCamel.com</title>

<link rel="stylesheet" type="text/css" href="../style.css?derp=derp" />
<link rel="stylesheet" type="text/css" href="../style-admin.css?derp=derp" />

<link rel="shortcut icon" href="favicon.ico">

<script language="javascript">
function togglemsgs() {
if(document.getElementById("Msgs").style.display == "inline") {
document.getElementById("Msgs").style.display = "none";
document.getElementById("ShowHideMsgs").innerHTML = "Show Messages";
}
else {
document.getElementById("Msgs").style.display = "inline";
document.getElementById("ShowHideMsgs").innerHTML = "Hide Messages";
}
}
function toggleother() {
if(document.getElementById("Other").style.display == "inline") {
document.getElementById("Other").style.display = "none";
document.getElementById("ShowHideOther").innerHTML = "Show Other";
}
else {
document.getElementById("Other").style.display = "inline";
document.getElementById("ShowHideOther").innerHTML = "Hide Other";
}
}
</script>

</head>
<body>

<div id="header">

</div>

<div id="toprocks">
</div>

<div id="main">
	
	<div id="menu">
		<ul class="menulist">
		<li><a href="../index.html">News</a></li>
		<li><a href="../downloads.html">Downloads</a></li>
		<li><a href="../code.html">Code</a></li>
		<li><a href="../gallery.html">Gallery</a></li>
		<li><a href="../contact.html">Contact</a></li>
		</ul>
	</div>
	
	<div id="content">

<?php
$user="a2207475_1";
$password="a2207475_2";
$database="a2207475_db";
mysql_connect("mysql2.000webhost.com",$user,$password);
@mysql_select_db($database) or die( "Unable to select database");
$query="SELECT * FROM msgs";
$result=mysql_query($query);

$num=mysql_num_rows($result);
mysql_close();

echo "<center><a href=\"javascript:togglemsgs();\" id=\"ShowHideMsgs\">Show Messages</a><font style=\"color:#930;text-decoration:none;border-bottom: 1px dotted #F96;\"> ($num)</font></center>\n";

echo "<br />\n
	<div id=\"Msgs\" style=\"display: none;\">";

$num -= 1;
while ($num >= 0) {

$id=str_replace("/;/",";",mysql_result($result,$num,"id"));
$first=str_replace("/;/",";",mysql_result($result,$num,"first"));
$last=str_replace("/;/",";",mysql_result($result,$num,"last"));
$email=str_replace("/;/",";",mysql_result($result,$num,"email"));
$tel=str_replace("/;/",";",mysql_result($result,$num,"tel"));
$comments=str_replace("/;/",";",mysql_result($result,$num,"comments"));
$date=mysql_result($result,$num,"date");

echo "<div class=\"msgtitlecontainer\">\n
	<i>$id</i> <b>Name</b> $first <b>Surname</b> $last <b>Email</b> $email <b>Phone</b> $tel <b>Date</b> $date \n
	</div>\n
	<div class=\"msgcontainer\">\n
	<b><font color=\"#993300\">>></font></b> $comments\n
	</div>\n";

$num--;
}
?>
<center><a href="javascript:togglemsgs();">Hide Messages</a></center>
<hr />
	</div>

<center><a href="javascript:toggleother();" id="ShowHideOther">Show Other</a></center>
<br />
<div id="Other" style="display: none;">
other
</div>
	</div>

	<div id="fix">
	</div>
</div>

<div id="bottomrocks">
</div>

<div id="footer">
Copyright &copy; Since 2008 - AstroCamel - Design by George Skouroupathis
</div>

</body>
</html>