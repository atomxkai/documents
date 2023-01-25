var start = 1;
var jump = 2;

//set up a loop to jump thru the document
for (var i=start; i<this.numPages; i=i+jump) {
//add the new page after page i+1.
this.newPage(i);
//skip the page you just added
i++;
}
