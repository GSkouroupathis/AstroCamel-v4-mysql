<form action="" method="post">
Your Message:<br />
<textarea rows="4" cols="30" name="decoded" id="decoded">
</textarea>
<hr />
<input type="submit" value="Start Encoding" />
</form>
<?php

//Declaring variables
$decoded = $_POST['decoded'];

for ($i=0; $i<strlen($decoded); $i++)
	{
	$asciii = ord(substr($decoded, $i, 1));
	$asciii = $asciii * ($i+1) + 1;
	if ($asciii > 255)
		{
		$a = floor(($asciii/255) + 0.000000005);
		$asciii = $asciii - ($a * 255);
		}
	$character = chr($asciii);
	$encoded = substr_replace($decoded,$character,$i,1);
	$decoded = $encoded;
	}

	echo "<textarea rows='4' cols='30'>$encoded</textarea>";

?>
</html>