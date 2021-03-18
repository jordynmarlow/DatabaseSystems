<?php

// Need to figure out how to host non locally
$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
// DB name in phpMyAdmin
$dbname = "baue3081";

if(!$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname))
{

	die("failed to connect!");
}
