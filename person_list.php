
<?php include_once("header.php");?>
<div class="container-fluid">
<h1>Person List</h1>
<?php
$sqlSelect = "SELECT pid, name, description, mjid, blood, mnid, sex, sjid, color, biography FROM person";
$resultSelect = $conn->query($sqlSelect);
?>
<table class="cell-border stripe">
<thead>
<tr>
<th>i</th>
<th>Pid</th>
<th>Name</th>
<th>Description</th>
<th>Mjid</th>
<th>Blood</th>
<th>Mnid</th>
<th>Sex</th>
<th>Sjid</th>
<th>Color</th>
<th>Biography</th>
<th>Action</th>
</tr>
</thead>
<tbody><?php
while ($row = $resultSelect -> fetch_row()) { ?>
<tr>
<td></td><td><?php echo $row[0]; ?></td><td><?php echo $row[1]; ?></td><td><?php echo $row[2]; ?></td><td><?php echo $row[3]; ?></td><td><?php echo $row[4]; ?></td><td><?php echo $row[5]; ?></td><td><?php echo $row[6]; ?></td><td><?php echo $row[7]; ?></td><td><?php echo $row[8]; ?></td><td><?php echo $row[9]; ?></td>
<td><a href="person_view.php?id=<?php echo $row[0]; ?>" title="View" target="_blank" class="alert-link"><i class="fas fa-eye"></i></a> <a href="person_edit.php?id=<?php echo $row[0]; ?>" title="Edit" target="_blank" class="alert-link"><i class="fas fa-edit"></i></a> <a class="delete_row alert-link" data-row-id="<?php echo $row[0]; ?>" href="javascript:void(0)" title="Delete" target="_blank"><i class="fas fa-trash-alt"></i></a> </td>
</tr>
<?php } ?>
</tbody>
<tfoot>
<tr>
<td>i</th>
<th>Pid</th>
<th>Name</th>
<th>Description</th>
<th>Mjid</th>
<th>Blood</th>
<th>Mnid</th>
<th>Sex</th>
<th>Sjid</th>
<th>Color</th>
<th>Biography</th>
<th>Action</th>
</tr>
</tfoot>
</table>
</div>
 <div id="myModal" class="modal fade"><div class="modal-dialog modal-confirm"><div class="modal-content"><div class="modal-header"><div class="icon-box"><i class="material-icons">&#xE5CD;</i></div><h4 class="modal-title">Are you sure?</h4> <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button></div><div class="modal-body"><p>Do you really want to delete these records? This process cannot be undone.</p></div><div class="modal-footer"><button type="button" class="btn btn-info" data-dismiss="modal">Cancel</button><button type="button" class="btn btn-danger">Delete</button></div></div></div></div> 
 <script>$(document).ready(function() {
 var titlePage = "Person List"; var siteName = "Py to CRUD PHP"; document.title = titlePage + " | " + siteName;
 var t=$("table").DataTable({columnDefs:[{searchable:!1,orderable:!1,targets:0},{targets:"_all",className:"dt-center"},{targets:[-1],className:"noExport"}],order:[[1,"asc"]],initComplete:function(){this.api().columns([1,2]).every(function(){var e=this,o=$('<select style="width:50px;"><option value="">All</option></select>').appendTo($(e.footer()).empty()).on("change",function(){var o=$.fn.dataTable.util.escapeRegex($(this).val());e.search(o?"^"+o+"$":"",!0,!1).draw()});e.data().unique().sort().each(function(e,n){o.append('<option value="'+e+'">'+e+"</option>")})})},dom:"lBfrtip",buttons:[{extend:"colvis",collectionLayout:"fixed columns",collectionTitle:"Show/hide columns",text:"Show/Hide"},{extend:"collection",text:"Export",buttons:[{extend:"print",exportOptions:{columns:":visible:not(.noExport)"},title:titlePage},{extend:"copy",exportOptions:{columns:":visible:not(.noExport)"},title:titlePage},{extend:"csv",exportOptions:{columns:":visible:not(.noExport)"},title:titlePage},{extend:"excel",exportOptions:{columns:":visible:not(.noExport)"},title:titlePage},{extend:"pdf",exportOptions:{columns:":visible:not(.noExport)"},title:titlePage}]}]});t.on("order.dt search.dt",function(){t.column(0,{search:"applied",order:"applied"}).nodes().each(function(e,o){e.innerHTML=o+1,t.cell(e).invalidate("dom")})}).draw();
 $(".delete_row").click(function(e){e.preventDefault();var t=$(this).attr("data-row-id"),a=$(this).parent("td").parent("tr");bootbox.dialog({message:"Are you sure you want to Delete ?",title:"<i class='fas fa-trash-alt'></i> Delete!",buttons:{success:{label:"Cancel",className:"btn-secondary",callback:function(){$(".bootbox").modal("hide");}},danger:{label:"Delete",className:"btn-danger",callback:function(){$.ajax({type:"POST",url:"person_delete.php",data:"id="+t}).done(function(e){bootbox.alert(e, function() {window.location.href=window.location.href;}),a.fadeOut("slow")}).fail(function(){bootbox.alert("Error...")})}}}})}); 
 $(".dataTables_length").prepend("<a class='btn btn-primary btn-sm' href='person_add.php' title='Add' target='_blank'><i class='fas fa-plus-circle'></i> New </a> ");
});</script>
<?php include_once("footer.php");?>