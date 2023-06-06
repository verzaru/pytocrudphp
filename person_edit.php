
<?php include_once("header.php");?>
<div class="container-fluid">
<h1>Edit Person</h1>
<?php if ($_SERVER["REQUEST_METHOD"] == "POST") {
$pid = $_POST["pid"];
$name = $_POST["name"];
$description = $_POST["description"];
$mjid = $_POST["mjid"];
$blood = $_POST["blood"];
$mnid = $_POST["mnid"];
$sex = $_POST["sex"];
$sjid = implode(",",$_POST["sjid"]);
$color = implode(",",$_POST["color"]);
$biography = $_POST["biography"];
$sqlUpdate = "UPDATE person SET pid = '$pid', name = '$name', description = '$description', mjid = '$mjid', blood = '$blood', mnid = '$mnid', sex = '$sex', sjid = '$sjid', color = '$color', biography = '$biography' WHERE pid=$pid";
$resultUpdate = $conn->query($sqlUpdate);
if ($resultUpdate === TRUE) {
echo '<div class="alert alert-success" role="alert">Edited the record successfully. Click <a href="person_view.php?id='.$pid.'" class="alert-link">here</a> to view detail or go back to <a href="person_list.php" class="alert-link">list</a>.</div>';
} else {
echo '<div class="alert alert-danger" role="alert">Error: '.$conn->error.'</div>';
}}?>
<?php if (!(isset($_GET))) {
echo '<div class="alert alert-warning" role="alert">Please specify ID in URL</div>';
} else {
$id = $_GET["id"];
$sqlSelect = "SELECT pid, name, description, mjid, blood, mnid, sex, sjid, color, biography FROM person WHERE pid = $id";
$resultSelect = $conn->query($sqlSelect);
while ($row = $resultSelect -> fetch_row()) { ?>
<form method="post" action="<?php echo $_SERVER['PHP_SELF'].'?id='.$id; ?>">
<table class="table table-bordered">
<tr><td style="width: 1%">1</td><td style="width: 1%"><label for="pid">Pid</label></td><td><?php echo $row[0]; ?><input type="hidden" name="pid" id="pid" value="<?php echo $row[0]; ?>"></td></tr>
<tr><td style="width: 1%">2</td><td style="width: 1%"><label for="name">Name</label></td><td><input type="text" name="name" id="name" value="<?php echo $row[1]; ?>" class="form-control"></td></tr>
<tr><td style="width: 1%">3</td><td style="width: 1%"><label for="description">Description</label></td><td><textarea name="description" id="description" class="form-control"><?php echo $row[2]; ?></textarea></td></tr>
<tr><td style="width: 1%">4</td><td style="width: 1%"><label for="mjid">Mjid</label></td><td><select name="mjid" id="mjid" class="form-control">
<?php $sqlSelect2 = "SELECT mjid,mjname FROM major";
 $resultSelect2 = $conn->query($sqlSelect2);
 while ($row2 = $resultSelect2 -> fetch_row()) { 
 if ($row2[0] == $row[3]) { ?><option value="<?php echo $row2[0]; ?>" selected ><?php echo $row2[1]; ?></option>
 <?php } else { ?><option value="<?php echo $row2[0]; ?>"><?php echo $row2[1]; ?></option>
 <?php } } ?></select></td></tr>
<tr><td style="width: 1%">5</td><td style="width: 1%"><label for="blood">Blood</label></td><td><select name="blood" id="blood" class="form-control">
<?php $arr = array("a"=>"A","b"=>"B","ab"=>"AB","o"=>"O",);
 foreach($arr as $k => $val) {
 if($row[4]==$k){?>
 <option value="<?php echo $k; ?>" selected ><?php echo $val; ?></option><?php
 } else { ?>
 <option value="<?php echo $k; ?>" ><?php echo $val; ?></option><?php 
 } }?></select></td></tr>
<tr><td style="width: 1%">6</td><td style="width: 1%"><label for="mnid">Mnid</label></td><td>
<?php $sqlSelect2 = "SELECT mnid,mnname FROM minor";
 $resultSelect2 = $conn->query($sqlSelect2);
 while ($row2 = $resultSelect2 -> fetch_row()) { 
 if ($row2[0] == $row[5]) { ?><input type="radio" name="mnid" value="<?php echo $row2[0]; ?>" checked > <?php echo $row2[1]." "; 
 } else { ?><input type="radio" name="mnid" value="<?php echo $row2[0]; ?>"> <?php echo $row2[1]." "; 
 } 
 } ?></td></tr>
<tr><td style="width: 1%">7</td><td style="width: 1%"><label for="sex">Sex</label></td><td>
<?php $arr = array("1"=>"Male","2"=>"Female",);
 foreach($arr as $k => $val) {
 if($row[6]==$k){?>
 <input type="radio" name="sex" value="<?php echo $k; ?>" checked > <?php echo $val; 
 } else { ?>
 <input type="radio" name="sex" value="<?php echo $k; ?>" > <?php echo $val; 
 } }?></td></tr>
<tr><td style="width: 1%">8</td><td style="width: 1%"><label for="sjid">Sjid</label></td><td>
<?php $sqlSelect3 = "SELECT sjid,sjname FROM subject"; 
 $arr_expl = explode(",",$row[7]); 
 $resultSelect3 = $conn->query($sqlSelect3);
 while ($row3 = $resultSelect3 -> fetch_row()) { 
 $set_checked = "";
 if(in_array($row3[0], $arr_expl)) {
 $set_checked = "checked";
 } ?>
 <input type="checkbox" name="sjid[]" value="<?php echo $row3[0]; ?>" <?php echo $set_checked; ?> > <?php echo $row3[1]; 
 }?></td></tr>
<tr><td style="width: 1%">9</td><td style="width: 1%"><label for="color">Color</label></td><td>
<?php $arr = array("red"=>"Red","green"=>"Green","blue"=>"Blue",);
 $arr_k = array_keys($arr);
 $arr_v = array_values($arr);
 $arr_expl = explode(",",$row[8]); 
 $n = 0;
 foreach($arr_k as $val) {
 $set_checked = "";
 if(in_array($val, $arr_expl)) {
 $set_checked = "checked"; 
 } ?>
 <input type="checkbox" name="color[]" value="<?php echo $val; ?>" <?php echo $set_checked; ?> > <?php echo $arr_v[$n]; 
  $n++;}?></td></tr>
<tr><td style="width: 1%">10</td><td style="width: 1%"><label for="biography">Biography</label></td><td><textarea name="biography" id="biography" class="summernote"><?php echo $row[9]; ?></textarea></td></tr>
<tr><td></td><td></td><td><input type="submit" name="btnPersonEdit" id="btnPersonEdit" value="Submit" class="btn btn-success"> <a href="person_list.php" class="btn btn-secondary" role="button">Cancel</a></td></tr>
</table>
</form>
<?php }} ?>
</div>
<script>$(document).ready(function() {
 document.title = "Edit Person | Py to CRUD PHP";
 $(".summernote").summernote({tabsize:2,height:120,toolbar:[["style",["style"]],["font",["bold","underline","clear"]],["color",["color"]],["para",["ul","ol","paragraph"]],["table",["table"]],["insert",["link","picture","video"]],["view",["fullscreen","codeview","help"]]]});
});</script>
<?php include_once("footer.php");?>