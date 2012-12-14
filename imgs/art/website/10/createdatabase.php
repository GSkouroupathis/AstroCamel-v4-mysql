<?
$user="f75_1";
$password="af";
$database="a220f_db";
mysql_connect("mysql2.000webhost.com",$user,$password);
@mysql_select_db($database) or die( "Unable to select database");
$query="CREATE TABLE msgs (id int(6) NOT NULL auto_increment,first varchar(20),last varchar(30),email varchar(50),tel varchar(15),comments text,date varchar(16),PRIMARY KEY (id))";
mysql_query($query);
mysql_close();
?>
