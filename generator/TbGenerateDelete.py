from TbConfig import * 
from TbGetInput import * 

action = 'delete'

class TbGenerateDelete():
	def __init__(self):
		fileObj = open("../"+tbName+"_"+action+".php", "w")
		fileObj.write('\n<?php include_once("config.php");?>')
		fileObj.write('\n<?php if($_REQUEST["id"]) {')
		fileObj.write('\n$id = $_POST["id"];')
		sqlDelete = "$sqlDelete = \"DELETE FROM "+tbName+" WHERE "+names[0]+"=$"+names[0]+"\";"
		fileObj.write('\n'+sqlDelete)
		fileObj.write('\n$resultDelete = $conn->query($sqlDelete);')
		fileObj.write('\nif ($resultDelete === TRUE) {')
		fileObj.write('\n echo "Deleted the record successfully.";')
		fileObj.write('\n} else {')
		fileObj.write('\n echo "Error deleting record: " . $conn->error;')
		fileObj.write('\n} } else {')
		fileObj.write('\n echo "Please specify ID."; } ?>')
		fileObj.close() 










