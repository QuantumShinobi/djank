const params = new URLSearchParams(window.location.search);

function clear_query_string() {
  var uri = window.location.toString();
  if (uri.indexOf("?") > 0) {
    var clean_uri = uri.substring(0, uri.indexOf("?"));
    window.history.replaceState({}, document.title, clean_uri);
  }
}
document.addEventListener("DOMContentLoaded", function () {
  if (params.get("doesnotexist") === "true") {
    document.getElementById("doesnotexist").style.display = "block";
    clear_query_string();
  }
  if (params.get("added") === "true") {
    document.getElementById("friend_added").style.display = "block";
    clear_query_string();
  }
});
