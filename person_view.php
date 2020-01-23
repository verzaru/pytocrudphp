
<?php include_once("header.php");?>
<div class="container-fluid">
<h1>View Person</h1>
<?php if (!(isset($_GET))) {
echo '<div class="alert alert-warning" role="alert">Please specify ID in URL</div>';
} else {
$id = $_GET["id"];
$sqlSelect = "SELECT pid, name, description, mjid, blood, mnid, sex, sjid, color, biography FROM person WHERE pid = $id";
$resultSelect = $conn->query($sqlSelect);
while ($row = $resultSelect -> fetch_row()) { ?>
<table class="table table-bordered">
<tr><td style="width: 1%">1</td><td style="width: 1%"><label for="pid">Pid</label></td><td><?php echo $row[0]; ?></td></tr>
<tr><td style="width: 1%">2</td><td style="width: 1%"><label for="name">Name</label></td><td><?php echo $row[1]; ?></td></tr>
<tr><td style="width: 1%">3</td><td style="width: 1%"><label for="description">Description</label></td><td><?php echo $row[2]; ?></td></tr>
<tr><td style="width: 1%">4</td><td style="width: 1%"><label for="mjid">Mjid</label></td><td>
<?php $sqlSelect2 = "SELECT mjid,mjname FROM major WHERE mjid = $row[3] ";
 $resultSelect2 = $conn->query($sqlSelect2);
 $row2 = $resultSelect2 -> fetch_row();
 echo $row2[1]; ?></td></tr>
<tr><td style="width: 1%">5</td><td style="width: 1%"><label for="blood">Blood</label></td><td>
<?php $arr = array("a"=>"A","b"=>"B","ab"=>"AB","o"=>"O",);
 foreach($arr as $k => $val) {
 if($row[4]==$k){
 echo $val; }} ?></td></tr>
<tr><td style="width: 1%">6</td><td style="width: 1%"><label for="mnid">Mnid</label></td><td>
<?php $sqlSelect2 = "SELECT mnid,mnname FROM minor WHERE mnid = $row[5] ";
 $resultSelect2 = $conn->query($sqlSelect2);
 $row2 = $resultSelect2 -> fetch_row();
 echo $row2[1]; ?></td></tr>
<tr><td style="width: 1%">7</td><td style="width: 1%"><label for="sex">Sex</label></td><td>
<?php $arr = array("1"=>"Male","2"=>"Female",);
 foreach($arr as $k => $val) {
 if($row[6]==$k){
 echo $val; }} ?></td></tr>
<tr><td style="width: 1%">8</td><td style="width: 1%"><label for="sjid">Sjid</label></td><td>
<?php $sqlSelect3 = "SELECT sjid,sjname FROM subject"; 
 $arr_expl = explode(",",$row[7]); 
 $resultSelect3 = $conn->query($sqlSelect3);
 while ($row3 = $resultSelect3 -> fetch_row()) { 
 if(in_array($row3[0], $arr_expl)) {
 echo $row3[1].", ";
 } 
 }?></td></tr>
<tr><td style="width: 1%">9</td><td style="width: 1%"><label for="color">Color</label></td><td>
<?php $arr = array("red"=>"Red","green"=>"Green","blue"=>"Blue",);
 $arr_k = array_keys($arr);
 $arr_v = array_values($arr);
 $arr_expl = explode(",",$row[8]); 
 $n = 0;
 foreach($arr_k as $val) {
 if(in_array($val, $arr_expl)) {
 echo $arr_v[$n].", "; 
 } 
  $n++;}?></td></tr>
<tr><td style="width: 1%">10</td><td style="width: 1%"><label for="biography">Biography</label></td><td><?php echo $row[9]; ?></td></tr>
<tr><td></td><td></td><td><a href="person_list.php" class="btn btn-secondary" role="button">Go to list</a></td></tr>
</table>
<?php }} ?>
</div>
<script>$(document).ready(function() {
	document.title = "View Person | Py to CRUD PHP";
});</script>
<?php include_once("footer.php");?>