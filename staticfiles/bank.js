function show() {
  div = document.getElementById("transactions");
  to_hide = document.getElementById("main");
  div.style.display = "block";
  to_hide.style.display = "none";
}
function back() {
  location.reload();
}

function add() {
  to_hide = document.getElementById("transactions");
  to_hide.style.display = "none";
  document.getElementById("add").style.display = "block";
}
function withdraw() {
  to_hide = document.getElementById("transactions");
  to_hide.style.display = "none";
  document.getElementById("withdraw").style.display = "block";
}
