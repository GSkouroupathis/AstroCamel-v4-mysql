<html>
<head>
<title>Page Hit Counter - By George Skouroupathis</title>
</head>
</html>
<?php

$hits = file_get_contents('hits.txt');
$hits += 1;

$file = fopen('hits.txt', 'w');
fwrite($file, $hits);
fclose($file);

echo "This page has been viewed $hits times.";

?>
