<?php

# Make sure you have the hits.txt file in the same directory as your PHP file

$hits = file_get_contents('hits.txt');
$hits += 1;

$file = fopen('hits.txt', 'w');
fwrite($file, $hits);
fclose($file);

echo "This page has been viewed $hits times.";

?>