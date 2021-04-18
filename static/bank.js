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

document.addEventListener("DOMContentLoaded", () => {
  add_btn = document.getElementById("add_btn");
  add_btn.onclick = () => {
    if (add_btn.disabled !== true) {
      add_btn.className = "btn btn-primary disabled";
      document.getElementById("add_form").submit();
    }
  };
  minus_btn = document.getElementById("minus_btn");
  minus_btn.onclick = () => {
    if (minus_btn.disabled !== true) {
      minus_btn.className = "btn btn-primary disabled";
      document.getElementById("minus_form").submit();
    }
  };
  document.addEventListener("keypress", function (event) {
    if (event.keyCode == 13) {
      // alert("hi.");
    }
  });
});
