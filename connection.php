<?php

$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$dbname = "baue3081";

if(!$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname))
{

	die("failed to connect!");
}
