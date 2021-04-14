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
  }
});
