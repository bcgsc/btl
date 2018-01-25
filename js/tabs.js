function openYear(evt, year) {

	var i, tabcontent, tablinks;

	// stop displaying all 
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i=0;i<tabcontent.length; i++){
		tabcontent[i].style.display="none";
	}
	
	document.getElementById(year).style.display = "block";

}

function openAll() {
    var i;
    var year = new Date().getFullYear();
    
    for (i=year; i>year-5; --i){
    document.getElementById(i.toString()).style.display = "block";
   }

}
