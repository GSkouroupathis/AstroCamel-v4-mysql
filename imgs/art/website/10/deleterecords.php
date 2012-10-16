<?
$user="a2207475_1";
$password="a2207475_2";
$database="a2207475_db";
mysql_connect("mysql2.000webhost.com",$user,$password);
@mysql_select_db($database) or die( "Unable to select database");
$query="DELETE FROM msgs";
mysql_query($query);
mysql_close();
?>