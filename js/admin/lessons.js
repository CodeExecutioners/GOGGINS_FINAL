
function AddPrivateLesson(){ 
$("#privateLessons tbody").append(
 "<tr id='None'>"+
 "<td class='type'>Private</td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='options'><button class='btnSave'value='save'>Save</button><button class='btnDelete'value='Delete'>Delete</button></td>"+
 "</tr>");
 $(".btnSave").bind("click", Save);
 $(".btnDelete").bind("click", Delete); 

};


function AddDropInLesson(){ 
$("#dropInLessons tbody").append(
 "<tr id='None'>"+
 "<td class='type'>Drop-In</td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='options'><button class='btnSave'value='save'>Save</button><button class='btnDelete'value='Delete'>Delete</button></td>"+
 "</tr>");
 $(".btnSave").bind("click", Save);
 $(".btnDelete").bind("click", Delete); 

};

function AddGroupLesson(){ 
$("#groupLessons tbody").append(
 "<tr id='None'>"+
 "<td class='type'>Group</td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='lesson'><input type='text'/></td>"+
 "<td class='options'><button class='btnSave'value='save'>Save</button><button class='btnDelete'value='Delete'>Delete</button></td>"+
 "</tr>");
 $(".btnSave").bind("click", Save);
 $(".btnDelete").bind("click", Delete); 

};


function Save(){ 

var par = $(this).parent().parent(); //tr 
 var tdType = par.children("td:nth-child(1)");
 var tdCity = par.children("td:nth-child(2)");
 var tdDate = par.children("td:nth-child(3)");
 var tdTime = par.children("td:nth-child(4)");
 var tdLocation = par.children("td:nth-child(5)");
 var tdCost = par.children("td:nth-child(6)");
 var tdButtons = par.children("td:nth-child(7)");
 tdType.html(tdType.children("input[type=text]").val()); 
 tdCity.html(tdCity.children("input[type=text]").val());
 tdDate.html(tdDate.children("input[type=text]").val());
 tdTime.html(tdTime.children("input[type=text]").val());
 tdLocation.html(tdLocation.children("input[type=text]").val());
 tdCost.html(tdCost.children("input[type=text]").val());
 tdButtons.html("<button class='btnEdit'value='Edit'>Edit</button><button class='btnDelete'value='Delete'>Delete</button>");
 $(".btnEdit").bind("click", Edit);
 $(".btnDelete").bind("click", Delete);
 }; 

 
 function Edit(){
 
 var par = $(this).parent().parent(); //tr 
 
 var tdType = par.children("td:nth-child(1)");
 var tdCity = par.children("td:nth-child(2)");
 var tdDate = par.children("td:nth-child(3)");
 var tdTime = par.children("td:nth-child(4)");
 var tdLocation = par.children("td:nth-child(5)");
 var tdCost = par.children("td:nth-child(6)");
 var tdButtons = par.children("td:nth-child(7)");

 tdCity.html("<input type='text' id='txtCity' value='"+tdCity.html()+"'/>");
 tdDate.html("<input type='text' id='txtDate' value='"+tdDate.html()+"'/>");
 tdTime.html("<input type='text' id='txtTime' value='"+tdTime.html()+"'/>");
 tdLocation.html("<input type='text' id='txtLocation' value='"+tdLocation.html()+"'/>");
 tdCost.html("<input type='text' id='txtCost' value='"+tdCost.html()+"'/>");
 tdButtons.html("<button class='btnSave'value='save'>Save</button>");
 $(".btnSave").bind("click", Save);
 $(".btnEdit").bind("click", Edit);
 $(".btnDelete").bind("click", Delete); 
 };

 function Delete(){
 var par = $(this).parent().parent(); //tr)
 var id = par.attr("id")
 var array  = {};
 var rowName = "ID";
 array[rowName] = id
 var json = JSON.stringify(array);
 //alert("DELETE JSON: " + json)
 json = "["+json+"]";
 alert("New JSON" + json);
 var path='/deleteLessons';
		$.ajax({
             type: 'POST',
			 url:path,
             data: json,
			 dataType: 'json',
			 contentType:'application/json; charset=utf-8',
             success: function(response) {
				alert("Success" + response)
				//alert('redirecting...');
				window.location = '/adminLessons';
             },error: function(response){
				//alert("Error with json post" + response);
			 
			}
			
			
		});
		return false;
	
	//postLessonsTable('#dropInLessons', path);
 };

 
 
 

 

function postLessonsTable(tableID, path){
    var keys = $(tableID +' tbody tr').map(function(i){
			id = this.id;
			return id;
	}).get()   
	
	
		
		//iterate through table
	var count = 0;
	var columns = $(tableID +' thead th').map(function() {
	  // This assumes that your headings are suitable to be used as
	  //  JavaScript object keys. If the headings contain characters 
	  //  that would be invalid, such as spaces or dashes, you should
	  //  use a regex here to strip those characters out.
	  count= count+1;
	  return $(this).text();
	  
	});
	
	columns[count-1] = "ID";
	
			$.each(columns, function( index, value ) {
				//alert( index + ": " + value );
			});
		
		var tableObject = $(tableID +' tbody tr').map(function(i) {
		  var row = {};

		 
		
		  var lastIndex = 0;
		  var id  = 0;
		  // Find all of the table cells on this row.
		  $(this).find('td').each(function(i) {
			// Determine the cell's column name by comparing its index
			//  within the row with the columns list we built previously.
			
				var rowName = columns[i];
				
				//alert("ID:" +id);
				// Add a new property to the row object, using this cell's
				//  column name as the key and the cell's text as the value.
				//alert("RowName: " + rowName)
				
				
				if(rowName == "ID"){
					row[rowName] =$(this).parent().attr("id");
				
				}else{
					row[rowName] =$(this).text();
				}
				
			
			
			
		  });
		  
		
		 
		  // Finally, return the row's object representation, to be included
		  //  in the array that $.map() ultimately returns.
		  
		  
		  return row;
		 
		// Don't forget .get() to convert the jQuery set to a regular array.
		}).get();
		
		
		
		jsonTable = JSON.stringify(tableObject);
		//alert("tableObject:" + jsonTable);
		
		
		
		$.ajax({
             type: 'POST',
			 url:path,
             data: jsonTable,
			 dataType: 'json',
			 contentType:'application/json; charset=utf-8',
             success: function(response) {
				//alert("Success" + response)
				//alert('redirecting...');
				window.location = '/adminLessons';
             },error: function(response){
				//alert("Error with json post" + response);
			 
			}
			
			
		});
		return false;
		
	};
	
	



$(document).ready(function() {


$(function(){ //Add, Save, Edit and Delete functions code
 $(".btnEdit").bind("click", Edit); 
 $(".btnDelete").bind("click", Delete);
 $(".btnSave").bind("click", Save);
 $("#btnAddPrivateLesson").bind("click", AddPrivateLesson);
 $("#btnAddDropInLesson").bind("click", AddDropInLesson);
 $("#btnAddGroupLesson").bind("click", AddGroupLesson);
 });
 
  //post for the drop in table
 $('#privateLessonsSaveTable').on('click', function (event) {
	event.preventDefault();
	path = '/adminLessons'
	postLessonsTable('#privateLessons', path);
 });

 
 
 
 //post for the drop in table
 $('#dropInLessonsSaveTable').on('click', function (event) {
	event.preventDefault();
	path = '/adminLessons'
	postLessonsTable('#dropInLessons', path);
 });

 
 //post for the group lessons table
 $('#groupLessonsSaveTable').on('click', function (event) {
		event.preventDefault();
    path = '/adminLessons'
	postLessonsTable('#groupLessons', path);
 });   
 
 
	$(".addLesson").on("click", function(event){
		//alert("adding Lesson");
		event.preventDefault();
		
		html  = $(".modal-body").html('');
		//$(".modal-footer").html("<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button><input type='submit' id='submitAddLesson' class='btn btn-primary' value='Add Lesson'></button>");
		
		$.ajax({
             type: 'GET',
			 url:'/addLesson',
             success: function(response) {
				//alert("Success" + response)
				$("#myModalLabel").html('Add Lesson');
				$(".modal-body").html(response);
				$("#myModal").modal('show'); //hide popup
				
				
             },error: function(response){
				alert("Error Adding Lesson");
			 
			}
			
			
		});
		
		event.stopImmediatePropagation();
		return false
	});
 
 
	$(".editLesson").on("click", function(event){
		//alert("editing Lesson");
		event.preventDefault();
	
		html  = $(".modal-body").html('');
		//$(".modal-footer").html("<button type='button' class='btn btn-default' data-dismiss='modal'>Close</button><input type='submit' id='submitEditLesson' class='btn btn-primary' value='Edit Lesson'></button>");
		//skip the "id" characters
		var lessonID = $(this).attr("id").substring(2);
		
		//alert("LessonID: " + lessonID);
		
	
		
		$.ajax({
             type: 'POST',
			 url:'/editLesson',
             data: lessonID,
             success: function(response) {
				//alert("Success" + response)
				$(".modal-body").html(response);
				$("#myModalLabel").html('Edit Lesson');
				$("#myModal").modal('show'); //hide popup
				
				
             },error: function(response){
				alert("Error Editing Lesson");
			 
			}
			
			
		});
		
		event.stopImmediatePropagation();
		return false
	});
	
	//on click for button
	
	$(".deleteLesson").on("click", function(event){
		//alert("deleting Lesson");
		event.preventDefault();

		var lessonID = $(this).attr("id").substring(2);
		//alert("LessonID: " + lessonID);
		
	
		
		$.ajax({
             type: 'POST',
			 url:'/deleteLesson',
             data: lessonID,
             success: function(response) {
				//alert("Success" + response)
				location.reload();
             },error: function(response){
				alert("Error Deleting Lesson");
			 
			}
			
			
		});
		
		event.stopImmediatePropagation();
		return false
	});
	
	
	
	
	
	
	
	
	
	
	
	$("#submitLesson").on("click", function(event){
			var form = $(".formLesson");
			if(form.valid()){
			
			var data = JSON.stringify(form.serializeArray())
			//alert(data);
			var path = '/updateLesson';
			$.ajax({
						type: 'POST',
			url:path,
						data: data,
			dataType: 'json',
			contentType:'application/json; charset=utf-8',
						success: function(response) {
			//alert("Success" + response)
			//alert('redirecting...');
			$("#myModal").modal('hide'); //hide popup
			location.reload();
						},error: function(response){
			alert("Error Saving");
			 
			}
			});
			event.stopImmediatePropagation();
			return false;
			}
			});
	
	
	//on click for button
	
	$(".deleteType").on("click", function(event){
		//alert("deleting Lesson");
		event.preventDefault();

		var typeID = $(this).attr("id").substring(2);
		//alert("LessonID: " + lessonID);
		
	
		
		$.ajax({
             type: 'POST',
			 url:'/deleteType',
             data: typeID,
             success: function(response) {
				//alert("Success" + response)
				location.reload();
             },error: function(response){
				alert("Error Deleting Type");
			 
			}
			
			
		});
		
		event.stopImmediatePropagation();
		return false
	});
	
	
	$(".deleteCity").on("click", function(event){
		//alert("deleting Lesson");
		event.preventDefault();

		var cityID = $(this).attr("id").substring(2);
		//alert("LessonID: " + lessonID);
		
	
		
		$.ajax({
             type: 'POST',
			 url:'/deleteCity',
             data: cityID,
             success: function(response) {
				//alert("Success" + response)
				location.reload();
             },error: function(response){
				alert("Error Deleting Type");
			 
			}
			
			
		});
		
		event.stopImmediatePropagation();
		return false
	});
	
	  
	
	/*
	
	
	
	$("#submitLesson").on("click", function(event){
		
		
		event.preventDefault()
		
	
		var form = $(".formLesson");
		
		
		var data = JSON.stringify(form.serializeArray())
		
		alert(data);
		var path = '/updateLesson';
		$.ajax({
             type: 'POST',
			 url:path,
             data: data,
			 dataType: 'json',
			 contentType:'application/json; charset=utf-8',
             success: function(response) {
				
				//alert("Success" + response)
				//alert('redirecting...');
				$("#myModal").modal('hide'); //hide popup
				location.reload();
				
				
             },error: function(response){
				alert("Error with json post" + response);
			 
			}
			
			
		});
		event.stopImmediatePropagation();
		return false;
		

		
		
	});
	
	 NOT USED
	
	$("#editLesson").on("click", function(event){
		
		event.preventDefault();
		
		$('input').each(function(){
		  $(this).attr('value', $(this).val());
		});
		alert("EDIT MODAL HTML: " + $("#myModalEdit").html());
		alert($("#editLessonForm").html());
		$("#editLessonForm").load
		var form = $("#editLessonForm");
		
		var data = JSON.stringify(form.serializeArray())
		
		
		alert(data);
		var path = '/lessons';
		$.ajax({
             type: 'POST',
			 url:path,
             data: data,
			 dataType: 'json',
			 contentType:'application/json; charset=utf-8',
             success: function(response) {
				
				alert("Success" + response)
				//alert('redirecting...');
				$("#myModalEdit").modal('hide'); //hide popup
				window.location = '/lessons';
             },error: function(response){
				alert("Error with json post" + response);
			 
			}
			
			
		});
		event.stopImmediatePropagation();
		return false;
	
	});
	
	*/
 });

 
 
 


 