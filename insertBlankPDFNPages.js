// Developed by Earl L
// Date: 14 January 2022
// JavaScript in Acrobat to insert N pages 

var start = 5; // add first page after N
var jump = 5; // add blank page after N pages

//set up a loop to jump thru the document
for (var i = start; i < this.numPages; i = i+jump) {
//add the new page after page i+1.
this.newPage(i);
//skip the page you just added
i++;
}
var finalPage = this.numPages
this.newPage(finalPage+1);
