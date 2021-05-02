function WarningPopup() {
  document.getElementById("popUp").style.display = "block";
}
function cancel() {
  document.getElementById("popUp").style.display = "none";
}
window.onclick = function (event) {
  if (event.target == document.getElementById("popUp")) {
    document.getElementById("popUp").style.display = "none";
  }
};
const isEmpty = (str) => !str.trim().length;
