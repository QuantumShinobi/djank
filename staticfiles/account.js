function show_pwd_form() {
  document.getElementById("pwd_form").style.display = "block";
  document.getElementById("main").style.display = "none";
}
function clear_query_string() {
  var uri = window.location.toString();
  if (uri.indexOf("?") > 0) {
    var clean_uri = uri.substring(0, uri.indexOf("?"));
    window.history.replaceState({}, document.title, clean_uri);
  }
}
function back() {
  location.reload();
}
const params = new URLSearchParams(window.location.search);
document.addEventListener("DOMContentLoaded", () => {
  if (params.get("pwd_change") === "true") {
    document.getElementById("pwd_change_alert").style.display = "block";
    clear_query_string();
  }
  if (params.get("t_list_erase") === "true") {
    document.getElementById("t_list_erase").style.display = "block";
    clear_query_string();
  }
  if (params.get("discord_account_linked") === "true") {
    document.getElementById("discord_account_linked").style.display = "block";
    clear_query_string();
  }
  if (params.get("discord_account_unlinked") === "true") {
    document.getElementById("discord_account_unlinked").style.display = "block";
    clear_query_string();
  }
  if (params.get("pwd_form") === "true") {
    show_pwd_form();
    clear_query_string();
  }
  if (params.get("format_incorrect") === "true") {
    document.getElementById("format_incorrect").style.display = "block";
    clear_query_string();
  }
  btn_submit = document.getElementById("add_mail_submit");
  btn_submit.onclick = () => {
    document.getElementById("non-animation").style.display = "none";
    document.getElementById("animation").style.display = "block";
  };
});

function link_discord() {
  document.getElementById("main").style.display = "none";
  document.getElementById("discord_form").style.display = "block";
}
function email_form() {
  document.getElementById("main").style.display = "none";
  document.getElementById("email_form").style.display = "block";
}
