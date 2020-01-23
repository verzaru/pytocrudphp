from TbConfig import * 
from TbGetInput import * 

action = 'edit'
btnName = 'btn'+tbName.capitalize()+action.capitalize()

class TbGenerateUpdate():
	def __init__(self):
		fileObj = open("../"+tbName+"_"+action+".php", "w")
		fileObj.write('\n<?php include_once("header.php");?>')
		fileObj.write('\n<div class="container-fluid">')
		fileObj.write('\n<h1>'+action.capitalize()+' '+tbName.capitalize()+'</h1>')
		fileObj.write('\n<?php if ($_SERVER["REQUEST_METHOD"] == "POST") {')
		for i in range(len(names)):
                        if "checkbox" in fieldInput[i] :
                                fileObj.write('\n$'+names[i]+' = implode(",",'+'$_POST["'+names[i]+'"]);')
                        else :
                                fileObj.write('\n$'+names[i]+' = '+'$_POST["'+names[i]+'"];')
		sqlUpdate = "$sqlUpdate = \"UPDATE "+tbName+" SET "
		for i in range(len(names)):
			sqlUpdate = sqlUpdate + names[i] + " = '$" + names[i] + "', " 
		sqlUpdate = sqlUpdate[0:-2] + " WHERE "+names[0]+"=$"+names[0]+"\";"
		fileObj.write('\n'+sqlUpdate)
		fileObj.write('\n$resultUpdate = $conn->query($sqlUpdate);')
		fileObj.write('\nif ($resultUpdate === TRUE) {')
		fileObj.write('\necho \'<div class="alert alert-success" role="alert">Edited the record successfully. Click <a href="'+tbName+'_view.php?id=\'.$'+names[0]+'.\'" class="alert-link">here</a> to view detail or go back to <a href="'+tbName+'_list.php" class="alert-link">list</a>.</div>\';')
		fileObj.write('\n} else {')
		fileObj.write('\necho \'<div class="alert alert-danger" role="alert">Error: \'.$conn->error.\'</div>\';')
		fileObj.write('\n}}?>')
		fileObj.write('\n<?php if (!(isset($_GET))) {')
		fileObj.write('\necho \'<div class="alert alert-warning" role="alert">Please specify ID in URL</div>\';')
		fileObj.write('\n} else {')
		fileObj.write('\n$id = $_GET["id"];')
		sqlSelect = "$sqlSelect = \"SELECT "
		for i in range(len(names)):
			sqlSelect = sqlSelect + names[i] + ", " 
		sqlSelect = sqlSelect[0:-2] + " FROM "+ tbName + " WHERE "+names[0]+" = $id\";"
		fileObj.write('\n'+sqlSelect)
		fileObj.write('\n$resultSelect = $conn->query($sqlSelect);')
		fileObj.write('\nwhile ($row = $resultSelect -> fetch_row()) { ?>')
		fileObj.write('\n<form method="post" action="<?php echo $_SERVER[\'PHP_SELF\'].\'?id=\'.$id; ?>">')
		fileObj.write('\n<table class="table table-bordered">')
		for i in range(len(names)):
			if i==0 :
				fileObj.write('\n<tr><td style="width: 1%">'+str(i+1)+'</td><td style="width: 1%"><label for="'+names[i]+'">'+names[i].capitalize()+'</label></td><td><?php echo $row['+str(i)+']; ?><input type="hidden" name="'+names[i]+'" id="'+names[i]+'" value="<?php echo $row['+str(i)+']; ?>"></td></tr>')
			else :
				fileObj.write('\n<tr><td style="width: 1%">'+str(i+1)+'</td><td style="width: 1%"><label for="'+names[i]+'">'+names[i].capitalize()+'</label></td><td>'+self.checkInput(fieldInput[i],i)+'</td></tr>')
		fileObj.write('\n<tr><td></td><td></td><td><input type="submit" name="'+btnName+'" id="'+btnName+'" value="Submit" class="btn btn-success"> <a href="'+tbName+'_list.php" class="btn btn-secondary" role="button">Cancel</a></td></tr>')
		fileObj.write('\n</table>')
		fileObj.write('\n</form>')
		fileObj.write('\n<?php }} ?>')
		fileObj.write('\n</div>')
		fileObj.write('\n<script>$(document).ready(function() {')
		fileObj.write('\n document.title = "'+action.capitalize()+' '+tbName.capitalize()+' | '+siteName+'";')
		fileObj.write('\n $(\".summernote\").summernote({tabsize:2,height:120,toolbar:[[\"style\",[\"style\"]],[\"font\",[\"bold\",\"underline\",\"clear\"]],[\"color\",[\"color\"]],[\"para\",[\"ul\",\"ol\",\"paragraph\"]],[\"table\",[\"table\"]],[\"insert\",[\"link\",\"picture\",\"video\"]],[\"view\",[\"fullscreen\",\"codeview\",\"help\"]]]});')
		fileObj.write('\n});</script>')
		fileObj.write('\n<?php include_once("footer.php");?>')
		fileObj.close() 
        
	def checkInput(self, type, i):
		resultInput = ''
		if type == "textarea" :
			resultInput = '<textarea name="'+names[i]+'" id="'+names[i]+'" class="form-control"><?php echo $row['+str(i)+']; ?></textarea>'
		if type == "editor" :
			resultInput = '<textarea name="'+names[i]+'" id="'+names[i]+'" class="summernote"><?php echo $row['+str(i)+']; ?></textarea>'
		elif type == "selectTb" :	
                    if len(selInputByTbUpdate) != 0 :
                        resultInput = '<select name="'+names[i]+'" id="'+names[i]+'" class="form-control">'
                        sqlSelect2 = "<?php $sqlSelect2 = \"SELECT "+selInputByTbUpdate[0][1]+","+selInputByTbUpdate[0][2]+" FROM "+ selInputByTbUpdate[0][0] + "\";"
                        resultInput += '\n'+sqlSelect2
                        resultInput += '\n $resultSelect2 = $conn->query($sqlSelect2);'
                        resultInput += '\n while ($row2 = $resultSelect2 -> fetch_row()) { '
                        resultInput += '\n if ($row2[0] == $row['+str(i)+']) { ?>'
                        resultInput += '<option value="<?php echo $row2[0]; ?>" selected ><?php echo $row2[1]; ?></option>'
                        resultInput += '\n <?php } else { ?>'
                        resultInput += '<option value="<?php echo $row2[0]; ?>"><?php echo $row2[1]; ?></option>'
                        resultInput += '\n <?php } } ?>'
                        resultInput += '</select>'
                        selInputByTbUpdate.pop(0)
		elif type == "selectCt" :
                        resultInput = '<select name="'+names[i]+'" id="'+names[i]+'" class="form-control">'
                        arr = '<?php $arr = array('
                        for j in range(len(selInputByCtUpdate[0])) :
                            arr += '"'+str(selInputByCtUpdate[0][j][0])+'"=>"'+str(selInputByCtUpdate[0][j][1])+'",'
                        arr[1:]
                        arr += ');'
                        resultInput += '\n'+arr    
                        resultInput += '\n foreach($arr as $k => $val) {'  
                        resultInput += '\n if($row['+str(i)+']==$k){?>'  
                        resultInput += '\n <option value="<?php echo $k; ?>" selected ><?php echo $val; ?></option><?php'  
                        resultInput += '\n } else { ?>'  
                        resultInput += '\n <option value="<?php echo $k; ?>" ><?php echo $val; ?></option><?php '  
                        resultInput += '\n } }?>'  
                        resultInput += '</select>'
                        selInputByCtUpdate.pop(0)
		elif type == "radioTb" :
                    if len(radInputByTbUpdate) != 0 :
                        sqlSelect2 = "<?php $sqlSelect2 = \"SELECT "+radInputByTbUpdate[0][1]+","+radInputByTbUpdate[0][2]+" FROM "+ radInputByTbUpdate[0][0] + "\";"
                        resultInput = '\n'+sqlSelect2
                        resultInput += '\n $resultSelect2 = $conn->query($sqlSelect2);'
                        resultInput += '\n while ($row2 = $resultSelect2 -> fetch_row()) { '
                        resultInput += '\n if ($row2[0] == $row['+str(i)+']) { ?>'
                        resultInput += '<input type="radio" name="'+names[i]+'" value="<?php echo $row2[0]; ?>" checked > <?php echo $row2[1]." "; '
                        resultInput += '\n } else { ?>'
                        resultInput += '<input type="radio" name="'+names[i]+'" value="<?php echo $row2[0]; ?>"> <?php echo $row2[1]." "; '
                        resultInput += '\n } '
                        resultInput += '\n } ?>'
                        radInputByTbUpdate.pop(0)
		elif type == "radioCt" :                        
                        arr = '<?php $arr = array('
                        for j in range(len(radInputByCtUpdate[0])) :
                            arr += '"'+str(radInputByCtUpdate[0][j][0])+'"=>"'+str(radInputByCtUpdate[0][j][1])+'",'
                        arr[1:]
                        arr += ');'
                        resultInput += '\n'+arr    
                        resultInput += '\n foreach($arr as $k => $val) {'  
                        resultInput += '\n if($row['+str(i)+']==$k){?>'  
                        resultInput += '\n <input type="radio" name="'+names[i]+'" value="<?php echo $k; ?>" checked > <?php echo $val; '  
                        resultInput += '\n } else { ?>'  
                        resultInput += '\n <input type="radio" name="'+names[i]+'" value="<?php echo $k; ?>" > <?php echo $val; '   
                        resultInput += '\n } }?>'
                        radInputByCtUpdate.pop(0)
		elif type == "checkboxTb" :
                    if len(chkInputByTbUpdate) != 0 :
                        sqlSelect3 = "<?php $sqlSelect3 = \"SELECT "+chkInputByTbUpdate[0][1]+","+chkInputByTbUpdate[0][2]+" FROM "+ chkInputByTbUpdate[0][0] + "\"; "
                        resultInput += '\n'+sqlSelect3
                        resultInput += '\n $arr_expl = explode(",",$row['+str(i)+']); '
                        resultInput += '\n $resultSelect3 = $conn->query($sqlSelect3);'
                        resultInput += '\n while ($row3 = $resultSelect3 -> fetch_row()) { '
                        resultInput += '\n $set_checked = "";'
                        resultInput += '\n if(in_array($row3[0], $arr_expl)) {' 
                        resultInput += '\n $set_checked = "checked";'
                        resultInput += '\n } ?>'
                        resultInput += '\n <input type="checkbox" name="'+names[i]+'[]" value="<?php echo $row3[0]; ?>" <?php echo $set_checked; ?> > <?php echo $row3[1]; '
                        resultInput += '\n }?>'
                        chkInputByTbUpdate.pop(0)

		elif type == "checkboxCt" :                        
                        arr = '<?php $arr = array('
                        for j in range(len(chkInputByCtUpdate[0])) :
                            arr += '"'+str(chkInputByCtUpdate[0][j][0])+'"=>"'+str(chkInputByCtUpdate[0][j][1])+'",'
                        arr[1:]
                        arr += ');'
                        resultInput += '\n'+arr  
                        resultInput += '\n $arr_k = array_keys($arr);'
                        resultInput += '\n $arr_v = array_values($arr);'  
                        resultInput += '\n $arr_expl = explode(",",$row['+str(i)+']); '
                        resultInput += '\n $n = 0;'
                        resultInput += '\n foreach($arr_k as $val) {' 
                        resultInput += '\n $set_checked = "";'
                                            
                        resultInput += '\n if(in_array($val, $arr_expl)) {'  
                        resultInput += '\n $set_checked = "checked"; '    
                        resultInput += '\n } ?>'  
                        resultInput += '\n <input type="checkbox" name="'+names[i]+'[]" value="<?php echo $val; ?>" <?php echo $set_checked; ?> > <?php echo $arr_v[$n]; '   
                        resultInput += '\n  $n++;}?>'
                        chkInputByCtUpdate.pop(0)
		else : 
			resultInput = '<input type="text" name="'+names[i]+'" id="'+names[i]+'" value="<?php echo $row['+str(i)+']; ?>" class="form-control">'
		return resultInput
