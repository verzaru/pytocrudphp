<!DOCTYPE html>
<html>
<head>
  <title>Pim</title>
	<link rel="stylesheet" type="text/css" href="lib/Bootstrap-4-4.1.1/css/bootstrap.min.css">
	<link rel="stylesheet" type="text/css" href="lib/fontawesome-free-5.12.0/css/fontawesome.css">
	<link rel="stylesheet" type="text/css" href="lib/fontawesome-free-5.12.0/css/solid.css">
	<link rel="stylesheet" type="text/css" href="lib/DataTables-1.10.20/css/jquery.dataTables.min.css">
	<link rel="stylesheet" type="text/css" href="lib/summernote-0.8.15/dist/summernote-lite.min.css">
	<script type="text/javascript" charset="utf8" src="lib/jQuery-3.4.1/jquery-3.4.1.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/Bootstrap-4-4.1.1/js/bootstrap.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/js/jquery.dataTables.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/Buttons-1.6.1/js/dataTables.buttons.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/Buttons-1.6.1/js/buttons.flash.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/JSZip-2.5.0/jszip.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/pdfmake-0.1.27/pdfmake.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/pdfmake-0.1.27/vfs_fonts.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/Buttons-1.6.1/js/buttons.html5.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/DataTables-1.10.20/plugins/Buttons-1.6.1/js/buttons.print.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/bootbox-5.4.0/bootbox.min.js"></script>
	<script type="text/javascript" charset="utf8" src="lib/summernote-0.8.15/summernote-lite.min.js"></script>
	<style>
	body { padding-top: 2rem;
	}
	.starter-template {
	  padding: 3rem 1.5rem;
	}
	h1 {
		margin-bottom: 1.7rem;
	}
	.dt-buttons {
		display: inline; 
		margin-left : 10px;
	}
	</style>
  </head>
<body>
<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
  <a class="navbar-brand" href="index.php">Py to CRUD PHP</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarCollapse">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link active" href="index.php">Home</a>
      </li>
	  <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="person_data" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Person</a>
        <div class="dropdown-menu" aria-labelledby="ship_data">
          <a class="dropdown-item" href="person_list.php">List Person</a>
          <a class="dropdown-item" href="person_add.php">Add Person</a>
        </div>
      </li>
    </ul>
  </div>
</nav>

<?php include_once("config.php");?>

<main role="main" class="container-fluid">
<div class="starter-template">

