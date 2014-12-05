function AddResource(){ 
$("#resourceTable tbody").append(
 "<tr>"+
 "<td><input type='text'/></td>"+
 "<td><input type='text'/></td>"+
 "<td><input type='text'/></td>"+
 "<td><input type='text'/></td>"+
 "<td><button class='btnSaveRes'value='SaveRes'>Save</button><button class='btnDelete'value='DeleteRes'>Delete</button></td>"+
 "</tr>");
 $(".btnSaveRes").bind("click", SaveRes);
 $(".btnDeleteRes").bind("click", DeleteRes); 

};
Save

function SaveRes(){ 

var par = $(this).parent().parent(); //tr 
 var type = par.children("td:nth-child(1)");
 var title = par.children("td:nth-child(2)");
 var linkOrAddress = par.children("td:nth-child(3)");
 var desc = par.children("td:nth-child(4)");
 var tdButtons = par.children("td:nth-child(5)");
 type.html(type.children("input[type=text]").val()); 
 title.html(title.children("input[type=text]").val()); 
 linkOrAddress.html(linkOrAddress.children("input[type=text]").val());
 desc.html(desc.children("input[type=text]").val());
 tdButtons.html("<button class='btnDeleteRes'value='DeleteRes'>Delete</button><button class='btnEditRes'value='EditRes'>Edit</button>");
 $(".btnEditRes").bind("click", EditRes);
 $(".btnDeleteRes").bind("click", DeleteRes);
 }; 

 
 function EditRes(){
 
 var par = $(this).parent().parent(); //tr 
 var type = par.children("td:nth-child(1)");
 var title = par.children("td:nth-child(2)");
 var linkOrAddress = par.children("td:nth-child(3)");
 var desc = par.children("td:nth-child(4)");
 var tdButtons = par.children("td:nth-child(5)");
 type.html("<input type='text' id='txtTitle' value='"+type.html()+"'/>");
 title.html("<input type='text' id='txtTitle' value='"+title.html()+"'/>");
 linkOrAddress.html("<input type='text' id='txtLink' value='"+linkOrAddress.html()+"'/>");
 desc.html("<input type='text' id='txtDesc' value='"+desc.html()+"'/>");
 tdButtons.html("<button class='btnSaveRes'value='SaveRes'>Save</button>");
 $(".btnSaveRes").bind("click", SaveRes);
 $(".btnEditRes").bind("click", EditRes);
 $(".btnDeleteRes").bind("click", DeleteRes); 
 };

 function DeleteRes(){
 var par = $(this).parent().parent(); //tr
 par.remove(); 
 
 }; 

 

$(document).ready(function() {


$(function(){ //Add, Save, Edit and Delete functions code
 $(".btnEditRes").bind("click", EditRes); 
 $(".btnDeleteRes").bind("click", DeleteRes);
 $(".btnSaveRes").bind("click", SaveRes);
 $("#btnAddResRow").bind("click", AddResource);
 });
 

 
$('#resourceSaveTable').on('click', function (event) {
		event.preventDefault();
        
		
		//iterate through table
	var columns = $('#resourceTable thead th').map(function() {
	  return $(this).text();
		});

		
		var tableObject = $('#resourceTable tbody tr').map(function(i) {
		  var row = {};
		 
		  // Find all of the table cells on this row.
		  $(this).find('td').each(function(i) {
			var rowName = columns[i];

			row[rowName] = $(this).text();
		  });
		 

		  return row;

		}).get();
		
		
		
		jsonTable = JSON.stringify(tableObject);
		//alert("tableObject:" + jsonTable);
		
		
		
		$.ajax({
             type: 'POST',
			 url:'/adminResources',
             data: jsonTable,
			 dataType: 'json',
			 contentType:'application/json; charset=utf-8',
             success: function(response) {
				//alert("Success" + response)
             },error: function(response){
				//alert("Error with json post" + response);
			 
			}
		});
		return false;
		
	});
	
});