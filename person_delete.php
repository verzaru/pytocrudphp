
<?php include_once("config.php");?>
<?php if($_REQUEST["id"]) {
$id = $_POST["id"];
$sqlDelete = "DELETE FROM person WHERE pid=$pid";
$resultDelete = $conn->query($sqlDelete);
if ($resultDelete === TRUE) {
 echo "Deleted the record successfully.";
} else {
 echo "Error deleting record: " . $conn->error;
} } else {
 echo "Please specify ID."; } ?>