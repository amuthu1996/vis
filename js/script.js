
function myfunc(filename, set){
//Creating a new AJAX request that will request 'test.csv' from the current directory
      $(".article").load('articles/'+filename, function(responseTxt, statusTxt, xhr){
        if(statusTxt == "error")
            alert("Error: " + xhr.status + ": " + xhr.statusText);
      });

      var img = $(".image").attr('src', 'images/' + set + '/' + filename + '.png').on('load', function() {
        if (!this.complete || typeof this.naturalWidth == "undefined" || this.naturalWidth == 0) {
            alert('broken image!');
        }
    });
}

$(document).ready(function(){
  w3IncludeHTML();
  myfunc('inp1.txt','set1');
  $(".but").click(function(){
    myfunc($('.dropdown').val(), $('.set').val());
  });

});
