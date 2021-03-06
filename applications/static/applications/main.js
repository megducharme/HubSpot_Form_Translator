function addDays(numberOfDays)
{
    let today = new Date(),
        dd = today.getDate() + numberOfDays,
        mm = today.getMonth()+1, //January is 0!
        yyyy = today.getFullYear();

    if(dd<10){
        dd='0'+dd
    }
    if(mm<10){
        mm='0'+mm
    }

    let computedDate = (mm+'/'+dd);

    return computedDate;
}


let TCD = ["TCD", "TCD-signed", "TCD-sent"]
for (var i=0;i<TCD.length;i++){
    $('<option/>').val(TCD[i]).html(TCD[i]).appendTo('#TCD');
}

let cohort = ["Cohort", "C32", "C33", "C34", "C35", "C36", "C37", "DA1", "E10", "DS3"]
for (var i=0;i<cohort.length;i++){
    $('<option/>').val(cohort[i]).html(cohort[i]).appendTo('#cohort');
}

let cohortSort = ["Cohort", "C32", "C33", "C34", "C35", "C36", "C37", "DA1", "E10", "DS3"]
for (var i=0;i<cohortSort.length;i++){
    $('<option/>').val(cohortSort[i]).html(cohortSort[i]).appendTo('#cohortSort');
}


let tuition = ["Tuition", "OPP", "REG", "REG(GI)", "Either"]
for (var i=0;i<tuition.length;i++){
    $('<option/>').val(tuition[i]).html(tuition[i]).appendTo('#tuition');
}

let local = ["Local/Remote", "Local", "Remote"]
for (var i=0;i<local.length;i++){
    $('<option/>').val(local[i]).html(local[i]).appendTo('#local');
}

let apptDate = ["Date", addDays(0), addDays(1), addDays(2), addDays(3), addDays(4)]
for (var i=0;i<apptDate.length;i++){
    $('<option/>').val(apptDate[i]).html(apptDate[i]).appendTo('#apptDate');
}

let time = ["Time", "2:30pm", "3:30pm", "4:30pm", "9:30am", "10:15am", "11:00am", "11:45am", "1:00pm", "8:00pm"]
for (var i=0;i<time.length;i++){
    $('<option/>').val(time[i]).html(time[i]).appendTo('#time');
}

let jumpStart = ["JS - N/A", "JS - Enrolled", "JS - In Class", "JS - Grad", "JS - Plan"]
for (var i=0;i<jumpStart.length;i++){
    $('<option/>').val(jumpStart[i]).html(jumpStart[i]).appendTo('#jumpStart');
}