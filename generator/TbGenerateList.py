from TbConfig import * 
from TbGetInput import * 

action = 'list'

class TbGenerateList():
	def __init__(self):
		fileObj = open("../"+tbName+"_"+action+".php", "w")
		fileObj.write('\n<?php include_once("header.php");?>')
		fileObj.write('\n<div class="container-fluid">')
		fileObj.write('\n<h1>'+action.capitalize()+' '+tbName.capitalize()+'</h1>')
		sqlSelect = "$sqlSelect = \"SELECT "
		for i in range(len(names)):
			sqlSelect = sqlSelect + names[i] + ", " 
		sqlSelect = sqlSelect[0:-2] + " FROM "+ tbName +"\";"
		fileObj.write('\n<?php')
		fileObj.write('\n'+sqlSelect)
		fileObj.write('\n$resultSelect = $conn->query($sqlSelect);')
		fileObj.write('\n?>')
		fileObj.write('\n<table class="table table-striped table-bordered">')
		fileObj.write('\n<thead>')
		fileObj.write('\n<tr>')
		fileObj.write('\n<th>i</th>')
		for i in range(len(names)):
			fileObj.write('\n<th>'+names[i].capitalize()+'</th>')
		fileObj.write('\n<th>Action</th>')
		fileObj.write('\n</tr>')
		fileObj.write('\n</thead>')
		fileObj.write('\n<tbody><?php')
		fileObj.write('\nwhile ($row = $resultSelect -> fetch_row()) { ?>')
		fileObj.write('\n<tr>')
		fileObj.write('\n<td></td>')
		for i in range(len(names)):
			fileObj.write('<td><?php echo $row['+str(i)+']; ?></td>')
		fileObj.write('\n<td><a href="'+tbName+'_view.php?id=<?php echo $row[0]; ?>" title="View" target="_blank" class="alert-link"><i class="fas fa-eye"></i></a> <a href="'+tbName+'_edit.php?id=<?php echo $row[0]; ?>" title="Edit" target="_blank" class="alert-link"><i class="fas fa-edit"></i></a> <a class="delete_row alert-link" data-row-id="<?php echo $row[0]; ?>" href="javascript:void(0)" title="Delete" target="_blank"><i class="fas fa-trash-alt"></i></a> </td>')
		fileObj.write('\n</tr>')
		fileObj.write('\n<?php } ?>')
		fileObj.write('\n</tbody>')
		fileObj.write('\n<tfoot>')
		fileObj.write('\n<tr>')
		fileObj.write('\n<td>i</th>')
		for i in range(len(names)):
			fileObj.write('\n<th>'+names[i].capitalize()+'</th>')
		fileObj.write('\n<th>Action</th>')
		fileObj.write('\n</tr>')
		fileObj.write('\n</tfoot>')
		fileObj.write('\n</table>')
		fileObj.write('\n</div>')
		fileObj.write('\n <div id="myModal" class="modal fade"><div class="modal-dialog modal-confirm"><div class="modal-content"><div class="modal-header"><div class="icon-box"><i class="material-icons">&#xE5CD;</i></div><h4 class="modal-title">Are you sure?</h4> <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button></div><div class="modal-body"><p>Do you really want to delete these records? This process cannot be undone.</p></div><div class="modal-footer"><button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button><button type="button" class="btn btn-danger">Delete</button></div></div></div></div> ')
		fileObj.write('\n<script>$(document).ready(function() {')
		fileObj.write('\n document.title = "'+action.capitalize()+' '+tbName.capitalize()+' | '+siteName+'";')
		fileObj.write('\n var t=$(\"table\").DataTable({columnDefs:[{searchable:!1,orderable:!1,targets:0}],order:[[1,\"asc\"]],initComplete:function(){this.api().columns([3,4]).every(function(){var e=this,t=$(\'<select style=\"width:50px;\"><option value=\"\">All</option></select>\').appendTo($(e.footer()).empty()).on(\"change\",function(){var t=$.fn.dataTable.util.escapeRegex($(this).val());e.search(t?\"^\"+t+\"$\":\"\",!0,!1).draw()});e.data().unique().sort().each(function(e,a){t.append(\'<option value=\"\'+e+\'\">\'+e+\"</option>\")})})},dom:\"Blfrtip\",buttons:[\"copy\",\"csv\",\"excel\",\"pdf\",\"print\"]});t.on(\"order.dt search.dt\",function(){t.column(0,{search:\"applied\",order:\"applied\"}).nodes().each(function(e,a){e.innerHTML=a+1,t.cell(e).invalidate(\"dom\")})}).draw(); ')
		fileObj.write('\n $(\".delete_row\").click(function(e){e.preventDefault();var t=$(this).attr(\"data-row-id\"),a=$(this).parent(\"td\").parent(\"tr\");bootbox.dialog({message:\"Are you sure you want to Delete ?\",title:\"<i class=\'fas fa-trash-alt\'></i> Delete!\",buttons:{success:{label:\"Cancel\",className:\"btn-secondary\",callback:function(){$(\".bootbox\").modal(\"hide\")}},danger:{label:\"Delete\",className:\"btn-danger\",callback:function(){$.ajax({type:\"POST\",url:\"'+tbName+'_delete.php\",data:\"id=\"+t}).done(function(e){bootbox.alert(e),a.fadeOut(\"slow\")}).fail(function(){bootbox.alert(\"Error...\")})}}}})}); ')
		fileObj.write('\n $(\".dataTables_length\").prepend(\"<a class=\'btn btn-primary btn-sm\' href=\''+tbName+'_add.php\' title=\'Add\' target=\'_blank\'><i class=\'fas fa-plus-circle\'></i> New </a> \");')
		fileObj.write('\n});</script>')
		fileObj.write('\n<?php include_once("footer.php");?>')
		fileObj.close() 
