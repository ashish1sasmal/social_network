// search when enter key is pressed
let search = document.getElementById("search");
search.input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    document.search.submit();
  }
});
