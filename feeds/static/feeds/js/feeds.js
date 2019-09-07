// search when enter key is pressed
let search = document.getElementById("search");
search.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.search.submit();
  }
});

let feel_button=document.getElementById("feel_button");
let feeling=document.getElementById("feeling");
feel_button.onclick=function(){
  feeling.style.display='block';
}

var photo=document.getElementsByClassName("photo");
var browse=document.getElementById("browse");
photo.onclick=function(e){
    e.preventDefault();
    browse.click();
}

browse.onclick=function(){
  alert("am available");
}