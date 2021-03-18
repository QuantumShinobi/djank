function show() {
  div = document.getElementById("transactions");
  to_hide = document.getElementById("main");
  div.style.display = "block";
  to_hide.style.display = "none";
}
function back() {
  to_hide = document.getElementById("transactions");
  to_hide.style.display = "none";
  div = document.getElementById("main");
  div.style.display = "block";
  add = document.getElementById("add");
  withdraw = document.getElementById("withdraw");
  add.style.display = "none";
  withdraw.style.display = "none";
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
