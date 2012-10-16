<html>
<head>
<title>Simple monoalphabetic Encoder - By George Skouroupathis</title>
</head>
<form action="" method="post">
Your Message:<br />
<textarea rows="10" cols="30" name="decoded" id="decoded">
</textarea>
<hr />
<input type="submit" value="Start Encoding" />
</form>
<?php

//Declaring variables
$decoded = $_POST['decoded'];

for ($i=0; $i<strlen($decoded); $i++)
	{
	$char = substr($decoded, $i, 1);
	$temp = ord($char);
	$temp++;
	if ($temp > 255)
		{
		$temp = $temp - 255;
		}
	$char = chr($temp);
	$encoded = substr_replace($decoded,$char,$i,1);
	$decoded = $encoded;
	}

	echo "<textarea rows='10' cols='30'>$encoded</textarea>";

?>
</html>