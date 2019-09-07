// search when enter key is pressed
let search = document.getElementById("search");
search.input.addEventListener("keyup", function(event) {
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