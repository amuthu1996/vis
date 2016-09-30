
function myfunc(filename){
//Creating a new AJAX request that will request 'test.csv' from the current directory
      $(".article").load('articles/'+filename, function(responseTxt, statusTxt, xhr){
        if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
      });

      var img = $(".image").attr('src', 'images/' + filename + '.png').on('load', function() {
        if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
            alert('broken image!');
        } else {
              alert("Epic Failure...lol");
        }
    });
}

$(document).ready(function(){
  w3IncludeHTML();
  myfunc('inp1.txt');
  $(".but").click(function(){
    myfunc($('.dropdown').val());
  });

});
