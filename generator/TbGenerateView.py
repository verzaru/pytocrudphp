from TbConfig import * 
from TbGetInput import * 

action = 'view'

class TbGenerateView():
	def __init__(self):
		fileObj = open("../"+tbName+"_"+action+".php", "w")
		fileObj.write('\n<?php include_once("header.php");?>')
		fileObj.write('\n<div class="container-fluid">')
		fileObj.write('\n<h1>'+action.capitalize()+' '+tbName.capitalize()+'</h1>')
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
		fileObj.write('\n<table class="table table-bordered">')
		for i in range(len(names)):
			fileObj.write('\n<tr><td style="width: 1%">'+str(i+1)+'</td><td style="width: 1%"><label for="'+names[i]+'">'+names[i].capitalize()+'</label></td><td>'+self.checkInput(fieldInput[i],i)+'</td></tr>')
		fileObj.write('\n<tr><td></td><td></td><td><a href="'+tbName+'_list.php" class="btn btn-secondary" role="button">Go to list</a></td></tr>')
		fileObj.write('\n</table>')
		fileObj.write('\n<?php }} ?>')
		fileObj.write('\n</div>')
		fileObj.write('\n<script>$(document).ready(function() {')
		fileObj.write('\n	document.title = "'+action.capitalize()+' '+tbName.capitalize()+' | '+siteName+'";')
		fileObj.write('\n});</script>')
		fileObj.write('\n<?php include_once("footer.php");?>')
		fileObj.close() 

	def checkInput(self, type, i):
		resultInput = ''
		if type == "selectTb" :	
                    if len(selInputByTbView) != 0 :
                        sqlSelect2 = "<?php $sqlSelect2 = \"SELECT "+selInputByTbView[0][1]+","+selInputByTbView[0][2]+" FROM "+ selInputByTbView[0][0] + " WHERE "+selInputByTbView[0][1]+" = $row["+str(i)+"] \";"
                        resultInput += '\n'+sqlSelect2
                        resultInput += '\n $resultSelect2 = $conn->query($sqlSelect2);'
                        resultInput += '\n $row2 = $resultSelect2 -> fetch_row();'
                        resultInput += '\n echo $row2[1]; ?>'
                        selInputByTbView.pop(0)
		elif type == "selectCt" :
                        arr = '<?php $arr = array('
                        for j in range(len(selInputByCtView[0])) :
                            arr += '"'+str(selInputByCtView[0][j][0])+'"=>"'+str(selInputByCtView[0][j][1])+'",'
                        arr[1:]
                        arr += ');'
                        resultInput += '\n'+arr    
                        resultInput += '\n foreach($arr as $k => $val) {'  
                        resultInput += '\n if($row['+str(i)+']==$k){'  
                        resultInput += '\n echo $val; }} ?>'  
                        selInputByCtView.pop(0)
		elif type == "radioTb" :
                    if len(radInputByTbView) != 0 :
                        sqlSelect2 = "<?php $sqlSelect2 = \"SELECT "+radInputByTbView[0][1]+","+radInputByTbView[0][2]+" FROM "+ radInputByTbView[0][0] + " WHERE "+radInputByTbView[0][1]+" = $row["+str(i)+"] \";"
                        resultInput += '\n'+sqlSelect2
                        resultInput += '\n $resultSelect2 = $conn->query($sqlSelect2);'
                        resultInput += '\n $row2 = $resultSelect2 -> fetch_row();'
                        resultInput += '\n echo $row2[1]; ?>'
                        radInputByTbView.pop(0)                  
		elif type == "radioCt" :                        
                        arr = '<?php $arr = array('
                        for j in range(len(radInputByCtView[0])) :
                            arr += '"'+str(radInputByCtView[0][j][0])+'"=>"'+str(radInputByCtView[0][j][1])+'",'
                        arr[1:]
                        arr += ');'
                        resultInput += '\n'+arr    
                        resultInput += '\n foreach($arr as $k => $val) {'  
                        resultInput += '\n if($row['+str(i)+']==$k){'  
                        resultInput += '\n echo $val; }} ?>'  
                        radInputByCtView.pop(0)
		elif type == "checkboxTb" :
                    if len(chkInputByTbView) != 0 :
                        sqlSelect3 = "<?php $sqlSelect3 = \"SELECT "+chkInputByTbView[0][1]+","+chkInputByTbView[0][2]+" FROM "+ chkInputByTbView[0][0] + "\"; "
                        resultInput += '\n'+sqlSelect3
                        resultInput += '\n $arr_expl = explode(",",$row['+str(i)+']); '
                        resultInput += '\n $resultSelect3 = $conn->query($sqlSelect3);'
                        resultInput += '\n while ($row3 = $resultSelect3 -> fetch_row()) { '
                        resultInput += '\n if(in_array($row3[0], $arr_expl)) {' 
                        resultInput += '\n echo $row3[1].", ";'
                        resultInput += '\n } '
                        resultInput += '\n }?>'
                        chkInputByTbView.pop(0)

		elif type == "checkboxCt" :                        
                        arr = '<?php $arr = array('
                        for j in range(len(chkInputByCtView[0])) :
                            arr += '"'+str(chkInputByCtView[0][j][0])+'"=>"'+str(chkInputByCtView[0][j][1])+'",'
                        arr[1:]
                        arr += ');'
                        resultInput += '\n'+arr  
                        resultInput += '\n $arr_k = array_keys($arr);'
                        resultInput += '\n $arr_v = array_values($arr);'  
                        resultInput += '\n $arr_expl = explode(",",$row['+str(i)+']); '
                        resultInput += '\n $n = 0;'
                        resultInput += '\n foreach($arr_k as $val) {' 
                        resultInput += '\n if(in_array($val, $arr_expl)) {'  
                        resultInput += '\n echo $arr_v[$n].", "; '    
                        resultInput += '\n } '  
                        resultInput += '\n  $n++;}?>'
                        chkInputByCtView.pop(0)
		else : 
			resultInput = '<?php echo $row['+str(i)+']; ?>'
		return resultInput