function show_pwd_form() {
  document.getElementById("pwd_form").style.display = "block";
  document.getElementById("main").style.display = "none";
}

function back() {
  location.reload();
}
const params = new URLSearchParams(window.location.search);
document.addEventListener("DOMContentLoaded", () => {
  if (params.get("pwd_change") === "true") {
    document.getElementById("pwd_change_alert").style.display = "block";
    var uri = window.location.toString();
    if (uri.indexOf("?") > 0) {
      var clean_uri = uri.substring(0, uri.indexOf("?"));
      window.history.replaceState({}, document.title, clean_uri);
    }
  }
  if (params.get("t_list_erase") === "true") {
    document.getElementById("t_list_erase").style.display = "block";
    var uri = window.location.toString();
    if (uri.indexOf("?") > 0) {
      var clean_uri = uri.substring(0, uri.indexOf("?"));
      window.history.replaceState({}, document.title, clean_uri);
    }
  }
});
