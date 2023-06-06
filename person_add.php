<?php include_once("header.php");?>
<div class="container-fluid">
<h1>Add Person</h1>
<?php if ($_SERVER["REQUEST_METHOD"] == "POST") {
 $name = $_POST["name"];
 $description = $_POST["description"];
 $mjid = $_POST["mjid"];
 $blood = $_POST["blood"];
 $mnid = $_POST["mnid"];
 $sex = $_POST["sex"];
 $sjid = implode(",",$_POST["sjid"]);
 $color = implode(",",$_POST["color"]);
 $biography = $_POST["biography"];
 $sqlInsert = "INSERT INTO person (name, description, mjid, blood, mnid, sex, sjid, color, biography) VALUES ('$name', '$description', '$mjid', '$blood', '$mnid', '$sex', '$sjid', '$color', '$biography')";
 $resultInsert = $conn->query($sqlInsert);
 if ($resultInsert === TRUE) {
 $last_id = $conn->insert_id;
 echo '<div class="alert alert-success" role="alert">Added a new record successfully. Click <a href="person_view.php?id='.$last_id.'" class="alert-link">here</a> to view detail or go back to <a href="person_list.php" class="alert-link">list</a>.</div>';
 } else {
 echo '<div class="alert alert-danger" role="alert">Error: '.$conn->error.'</div>';
 } 
 }?>
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
<table class="table table-bordered">
<tr><td style="width: 1%">1</td><td style="width: 1%"><label for="name">Name</label></td><td><input type="text" name="name" id="name" class="form-control"></td></tr>
<tr><td style="width: 1%">2</td><td style="width: 1%"><label for="description">Description</label></td><td><textarea name="description" id="description" class="form-control"></textarea></td></tr>
<tr><td style="width: 1%">3</td><td style="width: 1%"><label for="mjid">Mjid</label></td><td><select name="mjid" id="mjid" class="form-control">
 <?php $sqlSelect = "SELECT mjid,mjname FROM major";
 $resultSelect = $conn->query($sqlSelect);
 while ($row = $resultSelect -> fetch_row()) { ?>
 <option value="<?php echo $row[0]; ?>"><?php echo $row[1]; ?></option>
<?php } ?></select></td></tr>
<tr><td style="width: 1%">4</td><td style="width: 1%"><label for="blood">Blood</label></td><td><select name="blood" id="blood" class="form-control">
 <option value="a" >A</option>
 <option value="b" >B</option>
 <option value="ab" >AB</option>
 <option value="o" >O</option></select></td></tr>
<tr><td style="width: 1%">5</td><td style="width: 1%"><label for="mnid">Mnid</label></td><td>
<?php $sqlSelect = "SELECT mnid,mnname FROM minor";
 $resultSelect = $conn->query($sqlSelect);
 while ($row = $resultSelect -> fetch_row()) { ?>
 <input type="radio" name="mnid" value="<?php echo $row[0]; ?>"> <?php echo $row[1]; 
 } ?></td></tr>
<tr><td style="width: 1%">6</td><td style="width: 1%"><label for="sex">Sex</label></td><td>
 <input type="radio" name="sex" value="1"> Male 
 <input type="radio" name="sex" value="2"> Female </td></tr>
<tr><td style="width: 1%">7</td><td style="width: 1%"><label for="sjid">Sjid</label></td><td>
<?php $sqlSelect = "SELECT sjid,sjname FROM subject";
 $resultSelect = $conn->query($sqlSelect);
 while ($row = $resultSelect -> fetch_row()) { ?>
 <input type="checkbox" name="sjid[]" value="<?php echo $row[0]; ?>"> <?php echo $row[1]; 
 } ?></td></tr>
<tr><td style="width: 1%">8</td><td style="width: 1%"><label for="color">Color</label></td><td><input type="checkbox" name="color[]" value="red"> Red <input type="checkbox" name="color[]" value="green"> Green <input type="checkbox" name="color[]" value="blue"> Blue </td></tr>
<tr><td style="width: 1%">9</td><td style="width: 1%"><label for="biography">Biography</label></td><td><textarea name="biography" id="biography" class="summernote"></textarea></td></tr>
<tr><td></td><td></td><td><input type="submit" name="btnPersonAdd" id="btnPersonAdd" value="Submit" class="btn btn-success"> <a href="person_list.php" class="btn btn-secondary" role="button">Cancel</a></td></tr>
</table>
</form>
</div>
<script>$(document).ready(function() {
 document.title = "Add Person | Py to CRUD PHP";
 $(".summernote").summernote({tabsize:2,height:120,toolbar:[["style",["style"]],["font",["bold","underline","clear"]],["color",["color"]],["para",["ul","ol","paragraph"]],["table",["table"]],["insert",["link","picture","video"]],["view",["fullscreen","codeview","help"]]]});
});</script>
<?php include_once("footer.php");?>