<?php include_once("header.php");?>
<div class="container-fluid">
<h1>Home</h1>
<div class="row">

  <div class="col-md-4 mb-4">
	<div class="card">
	  <h5 class="card-header text-center">
		Person
	  </h5>
	  <div class="card-body">
		<ul>
			<li><a class="dropdown-item" href="person_list.php">List Person</a></li>
			<li><a class="dropdown-item" href="person_add.php">Add Person</a></li>
		</ul>
	  </div>
	  <div class="card-footer text-muted">
		9 fields
	  </div>
	</div>
  </div>

</div>
</div>
<script>$(document).ready(function() {
	document.title = "Home | Py to CRUD PHP";
});</script>
<?php include_once("footer.php");?>