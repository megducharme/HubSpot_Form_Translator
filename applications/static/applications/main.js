var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
 if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("date").defaultValue = today


let TCD = ["TCD", "TCD-signed", "TCD-sent"]
for (var i=0;i<TCD.length;i++){
    $('<option/>').val(TCD[i]).html(TCD[i]).appendTo('#TCD');
 }

let cohort = ["Cohort", "C26", "C27", "C28", "C29", "C30", "C31", "E7", "E8", "E9", "E10"]
for (var i=0;i<cohort.length;i++){
    $('<option/>').val(cohort[i]).html(cohort[i]).appendTo('#cohort');
 }


let tuition = ["Tuition", "OPP", "REG"]
for (var i=0;i<tuition.length;i++){
    $('<option/>').val(tuition[i]).html(tuition[i]).appendTo('#tuition');
 }

let local = ["Local/Remote", "Local", "Remote"]
for (var i=0;i<local.length;i++){
    $('<option/>').val(local[i]).html(local[i]).appendTo('#local');
 }


$('#date').html(mm + "/" + dd)

let time = ["Time", "2:30pm", "3:30pm", "4:30pm", "8:00am"]
for (var i=0;i<time.length;i++){
    $('<option/>').val(time[i]).html(time[i]).appendTo('#time');
 }