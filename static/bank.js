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

function transfer() {
  to_hide = document.getElementById("transactions");
  to_hide.style.display = "none";
  document.getElementById("transfer").style.display = "block";
}
document.addEventListener("DOMContentLoaded", () => {
  add_btn = document.getElementById("add_btn");
  add_btn.onclick = () => {
    document.getElementById("non-animation").style.display = "none";
    document.getElementById("animation").style.display = "block";
    document.getElementById("add_form").submit();
  };
  minus_btn = document.getElementById("minus_btn");
  minus_btn.onclick = () => {
    document.getElementById("non-animation").style.display = "none";
    document.getElementById("animation").style.display = "block";
    document.getElementById("minus_form").submit();
  };
  transfer_btn = document.getElementById("transfer_btn");
  transfer_btn.onclick = () => {
    document.getElementById("non-animation").style.display = "none";
    document.getElementById("animation").style.display = "block";
    document.getElementById("minus_form").submit();
  };
});
function clear_query_string() {
  var uri = window.location.toString();
  if (uri.indexOf("?") > 0) {
    var clean_uri = uri.substring(0, uri.indexOf("?"));
    window.history.replaceState({}, document.title, clean_uri);
  }
}

const params = new URLSearchParams(window.location.search);
document.addEventListener("DOMContentLoaded", () => {
  if (params.get("withdraw_form") === "true") {
    show();
    withdraw();
    clear_query_string();
  }
  if (params.get("add_form") === "true") {
    show();
    add();
    clear_query_string();
  }
  // transfer_form=true&amount_less=true
  if (params.get("transfer_form") === "true") {
    show();
    transfer();
    clear_query_string();
  }
  if (
    params.get("transfer_form") === "true" &&
    params.get("amount_less") === "true"
  ) {
    document.getElementById("amount_less").style.display = "block";
    show();
    transfer();
    clear_query_string();
  }
  if (params.get("transferred") === "true") {
    document.getElementById("transferred").style.display = "block";
    clear_query_string();
  }
  if (params.get("email_added") === "true") {
    document.getElementById("email_added").style.display = "block";
    clear_query_string();
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
