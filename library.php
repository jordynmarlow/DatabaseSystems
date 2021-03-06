<?php 
session_start();

	include("connection.php");
	include("functions.php");

	$user_data = check_login($con);

?>

<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<title>Library Database Management System</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
body {
    background-color: #eeeeee;
}

.top {
    background-color: #777777;
}

.btn {
    background-color: #777777;
    border: none;
    color: white;
    padding: 12px 16px;
    font-size: 16px;
    cursor: pointer;
}

.btn:hover {
    background-color: dodgerblue;
}

.search {
    background-color: #eaeaea;
}

.search input[type=text] {
    border: none;
    color: black;
    margin: 8px;
    font-size: 16px;
}

.search input[type=checkbox] {
    font-size: 16px;
}

#main {
  transition: margin-left .5s;
  padding: 20px;
}

.sidenav {
  height: 100%;
  width: 0; /* 0 width - change this with JavaScript */
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #333333;
  overflow-x: hidden; /* Disable horizontal scroll */
  padding-top: 60px; /* Place content 60px from the top */
  transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;
}

.sidenav a:hover {
  color: #eeeeee;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
}

table, th, td{
    border: 1px solid black;
}

</style>
<script>
    function openNav() {
        document.getElementById("sidenav").style.width = "300px";
    }

    function closeNav() {
        document.getElementById("sidenav").style.width = "0";
    }
</script>
<body>

<div class="top">
    <button onClick="openNav()" class="btn"><i class="fa fa-bars"></i></button>
    <button class="btn"><i class="fa fa-home"></i> Home</button>
    <button class="btn"><i class="fa fa-user-circle"></i> Profile</button>
</div>

<div class="search">
   <form>
        <input type="text" placeholder="Search All Books..." size="100" name = "valueSearch"> 
        <input type="checkbox" id="available_cb" name="available_cb">
        <label for="available_cb"> available books</label><br>
    <form>
</div>

<div id="sidenav" class="sidenav">
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
    <a href="signup.php">Create an account</a>
    <a href="#">Check in</a>
    <a href="#">Check out</a>
    <a href="logout.php">Sign out</a>
  </div>

  <div id="main">
      
      <?php
      if(isset($_POST['valueSearch'])){
        $search = $_POST['valueSearch'];
        $sql = "select * from books where CONCAT('title', 'author', 'genre', 'year', 'isbn')  like '%" . $search ."%'";
        $result = $con -> query($sql);
  
        if($result-> num_rows > 0 ){
            echo "<table><tr><th>Title</th><th>Author</th><th>Genre</th><th>Year</th><th>ISBN</th></tr>";
            while($row = $result -> fetch_assoc()) {
                echo "<tr><td>" . $row["title"]. "</td><td>" . $row["author"]. "</td><td>" . $row["genre"]. "</td><td>" . $row["year"]."</td><td>" . $row["isbn"]. "</td></tr>";
            }
            echo "</table>";
        } else {
            echo "0 results";
        }
      } else{
      $sql = "select * from books";
      $result = $con -> query($sql);

      if($result-> num_rows > 0 ){
          echo "<table><tr><th>Title</th><th>Author</th><th>Genre</th><th>Year</th><th>ISBN</th></tr>";
          while($row = $result -> fetch_assoc()) {
              echo "<tr><td>" . $row["title"]. "</td><td>" . $row["author"]. "</td><td>" . $row["genre"]. "</td><td>" . $row["year"]."</td><td>" . $row["isbn"]. "</td></tr>";
          }
          echo "</table>";
      } else {
          echo "0 results";
      }
    }
      ?>
      
  </div>

</body>
</html>