<!DOCTYPE html>
<html>
<head>
  <title>Pim</title>

  <link rel="stylesheet" type="text/css" href="lib/bootstrap-5.3.0/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="lib/fontawesome-free-6.4.0/css/fontawesome.min.css">
  <link rel="stylesheet" type="text/css" href="lib/fontawesome-free-6.4.0/css/solid.min.css">
  <link rel="stylesheet" type="text/css" href="lib/DataTables/dataTables.min.css">
  <link rel="stylesheet" type="text/css" href="lib/DataTables/DataTables-1.13.4/css/jquery.dataTables.min.css">

  <script type="text/javascript" charset="utf8" src="lib/jQuery-3.7.0/jquery-3.7.0.min.js"></script>
  <script type="text/javascript" charset="utf8" src="lib/popperjs-2.11.8/popper.min.js"></script>
  <script type="text/javascript" charset="utf8" src="lib/bootstrap-5.3.0/js/bootstrap.min.js"></script>
  <script type="text/javascript" charset="utf8" src="lib/bootbox-6.0.0/bootbox.min.js"></script>
  <script type="text/javascript" charset="utf8" src="lib/DataTables/DataTables-1.13.4/js/jquery.dataTables.min.js"></script>
  <script type="text/javascript" charset="utf8" src="lib/DataTables/Buttons-2.3.6/js/dataTables.buttons.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables/JSZip-2.5.0/jszip.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables/pdfmake-0.2.7/pdfmake.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables/pdfmake-0.2.7/vfs_fonts.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables/Buttons-2.3.6/js/buttons.html5.min.js"></script>
  <script type="text/javascript" charset="utf8" src="lib/DataTables/Buttons-2.3.6/js/buttons.colVis.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables/Buttons-2.3.6/js/buttons.print.min.js"></script>
  
  

	<link rel="stylesheet" type="text/css" href="lib/summernote-0.8.18/summernote-bs4.min.css">
	<script type="text/javascript" charset="utf8" src="lib/summernote-0.8.18/summernote-bs4.min.js"></script>

 	<style>


body { padding-top: 1.5rem;}
.starter-template { padding: 3rem 1.2rem;}
h1 { margin-bottom: 1.5rem;}
/* table.dataTable { border: 1px solid rgba(0, 0, 0, 0.3); } */ 
.dataTables_length { display:inline;}
.dataTables_filter { display:inline; float:right;}
.dt-buttons { display: inline; margin-left : 10px; }
button.dt-button, div.dt-button, a.dt-button, input.dt-button { padding: 0.5em 0.8em; }

	</style>
  </head>
<body>

<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="index.php">Py to CRUD PHP</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav me-auto mb-2 mb-md-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="index.php">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="#">About</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="person_data" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Person
          </a>
          <ul class="dropdown-menu" aria-labelledby="person_data">
          <a class="dropdown-item" href="person_list.php">List Person</a>
          <a class="dropdown-item" href="person_add.php">Add Person</a>
          <!-- <li><hr class="dropdown-divider"></li> -->
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>

<?php include_once("config.php");?>

<main role="main" class="container-fluid">
<div class="starter-template">

