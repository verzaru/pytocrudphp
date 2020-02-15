from TbGetInput import * 

names = names[1:]
fieldInput = fieldInput[1:]
action = 'add'
btnName = 'btn'+tbName.capitalize()+action.capitalize()

class TbGenerateInsert():
	def __init__(self):
                fileObj = open("../"+tbName+"_"+action+".php", "w")
                fileObj.write('<?php include_once("header.php");?>')
                fileObj.write('\n<div class="container-fluid">')
                fileObj.write('\n<h1>'+action.capitalize()+' '+tbName.capitalize()+'</h1>')
                fileObj.write('\n<?php if ($_SERVER["REQUEST_METHOD"] == "POST") {')
                for i in range(len(names)):
                        if "checkbox" in fieldInput[i] :
                                fileObj.write('\n $'+names[i]+' = implode(",",'+'$_POST["'+names[i]+'"]);')
                        else :
                                fileObj.write('\n $'+names[i]+' = '+'$_POST["'+names[i]+'"];')
                addSql = "\n $sqlInsert = \"INSERT INTO "+tbName+" ("
                for i in range(len(names)):
                        addSql = addSql + names[i] + ", "
                addSql = addSql[0:-2] + ") VALUES ("
                for i in range(len(names)):
                        addSql = addSql + "'$" + names[i] + "', "
                addSql = addSql[0:-2] + ")\";"
                fileObj.write(addSql)
                fileObj.write('\n $resultInsert = $conn->query($sqlInsert);')
                fileObj.write('\n if ($resultInsert === TRUE) {')
                fileObj.write('\n $last_id = $conn->insert_id;')
                fileObj.write('\n echo \'<div class="alert alert-success" role="alert">Added a new record successfully. Click <a href="'+tbName+'_view.php?id=\'.$last_id.\'" class="alert-link">here</a> to view detail or go back to <a href="'+tbName+'_list.php" class="alert-link">list</a>.</div>\';')
                fileObj.write('\n } else {')
                fileObj.write('\n echo \'<div class="alert alert-danger" role="alert">Error: \'.$conn->error.\'</div>\';')
                fileObj.write('\n } \n }?>')
                fileObj.write('\n<form method="post" action="<?php echo $_SERVER[\'PHP_SELF\'];?>">')
                fileObj.write('\n<table class="table table-bordered">')
                for i in range(len(names)):
                        fileObj.write('\n<tr><td style="width: 1%">'+str(i+1)+'</td><td style="width: 1%"><label for="'+names[i]+'">'+names[i].capitalize()+'</label></td><td>'+self.checkInput(fieldInput[i],i)+'</td></tr>')
                fileObj.write('\n<tr><td></td><td></td><td><input type="submit" name="'+btnName+'" id="'+btnName+'" value="Submit" class="btn btn-success"> <a href="'+tbName+'_list.php" class="btn btn-secondary" role="button">Cancel</a></td></tr>')
                fileObj.write('\n</table>')
                fileObj.write('\n</form>')
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
			resultInput = '<textarea name="'+names[i]+'" id="'+names[i]+'" class="form-control"></textarea>'
		elif type == "editor" :
			resultInput = '<textarea name="'+names[i]+'" id="'+names[i]+'" class="summernote"></textarea>'
		elif type == "selectTb" :	
                    if len(selInputByTbInsert) != 0 :
                        resultInput = '<select name="'+names[i]+'" id="'+names[i]+'" class="form-control">'
                        sqlSelect = "<?php $sqlSelect = \"SELECT "+selInputByTbInsert[0][1]+","+selInputByTbInsert[0][2]+" FROM "+ selInputByTbInsert[0][0] + "\";"
                        resultInput += '\n '+sqlSelect
                        resultInput += '\n $resultSelect = $conn->query($sqlSelect);'
                        resultInput += '\n while ($row = $resultSelect -> fetch_row()) { ?>'
                        resultInput += '\n <option value="<?php echo $row[0]; ?>"><?php echo $row[1]; ?></option>'
                        resultInput += '\n<?php } ?>'
                        resultInput += '</select>'
                        selInputByTbInsert.pop(0)
		elif type == "selectCt" :
                        resultInput = '<select name="'+names[i]+'" id="'+names[i]+'" class="form-control">'
                        for j in range(len(selInputByCtInsert[0])) :
                              resultInput += '\n <option value="'+str(selInputByCtInsert[0][j][0])+'" >'+str(selInputByCtInsert[0][j][1])+'</option>'  
                        resultInput += '</select>'
                        selInputByCtInsert.pop(0)
		elif type == "radioTb" :	
                    if len(radInputByTbInsert) != 0 :
                        sqlSelect = "<?php $sqlSelect = \"SELECT "+radInputByTbInsert[0][1]+","+radInputByTbInsert[0][2]+" FROM "+ radInputByTbInsert[0][0] + "\";"
                        resultInput = '\n'+sqlSelect
                        resultInput += '\n $resultSelect = $conn->query($sqlSelect);'
                        resultInput += '\n while ($row = $resultSelect -> fetch_row()) { ?>'
                        resultInput += '\n <input type="radio" name="'+names[i]+'" value="<?php echo $row[0]; ?>"> <?php echo $row[1]; '
                        resultInput += '\n } ?>'
                        radInputByTbInsert.pop(0)
		elif type == "radioCt" :
                        for j in range(len(radInputByCtInsert[0])) :
                              resultInput += '\n <input type="radio" name="'+names[i]+'" value="'+str(radInputByCtInsert[0][j][0])+'"> '+str(radInputByCtInsert[0][j][1])+' '  
                        radInputByCtInsert.pop(0)
		elif type == "checkboxTb" :	
                    if len(chkInputByTbInsert) != 0 :
                        sqlSelect = "<?php $sqlSelect = \"SELECT "+chkInputByTbInsert[0][1]+","+chkInputByTbInsert[0][2]+" FROM "+ chkInputByTbInsert[0][0] + "\";"
                        resultInput = '\n'+sqlSelect
                        resultInput += '\n $resultSelect = $conn->query($sqlSelect);'
                        resultInput += '\n while ($row = $resultSelect -> fetch_row()) { ?>'
                        resultInput += '\n <input type="checkbox" name="'+names[i]+'[]" value="<?php echo $row[0]; ?>"> <?php echo $row[1]; '
                        resultInput += '\n } ?>'
                        chkInputByTbInsert.pop(0)
		elif type == "checkboxCt" :
                        for j in range(len(chkInputByCtInsert[0])) :
                                resultInput += '<input type="checkbox" name="'+names[i]+'[]" value="'+str(chkInputByCtInsert[0][j][0])+'"> '+str(chkInputByCtInsert[0][j][1])+' '
                        chkInputByCtInsert.pop(0)
		else : 
			resultInput = '<input type="text" name="'+names[i]+'" id="'+names[i]+'" class="form-control">'
		return resultInput
		
