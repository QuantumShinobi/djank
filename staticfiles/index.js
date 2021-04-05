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

// function getDiscordCookie() {
//   var cookies = document.cookie
//     .split(";")
//     .map((cookie) => cookie.split("="))
//     .reduce(
//       (accumulator, [key, value]) => ({
//         ...accumulator,
//         [key.trim]: decodeURIComponent(value),
//       }),
//       {}
//     );
//   console.log(cookies["user-identity"]);
// }
