<form action="" method="post">
MD5 Hash: (in HEX)
<input type="text" name="md5hash" id="md5hash" />
<br />
Start from:
<input type="text" name="startvalue" id="md5hash" />
<br />
<input type="submit" value="Start Attack" />
</form>

<?php
//Declaring variables
$md5hash = $_POST['md5hash'];
$startvalue = $_POST['startvalue'];

if (isset($startvalue, $md5hash)) {
	$testvalue = $startvalue;

	while (md5($testvalue) != $md5hash) {
		$testvalue++; }

	echo "Your password is $testvalue";
				}
?>