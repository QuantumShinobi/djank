// const https = require("https");

// const data = JSON.stringify({
//   name: "rishit",
//   password: "okokokok",
//   id: 12345,
//   discord_username: "Rishit#8888",
//   bot_key: process.env.SECRET_KEY_DJANGO_BANK,
// });

// const options = {
//   hostname: "http://127.0.0.1:8000/",
//   path: "/api/login",
//   method: "POST",
//   headers: {
//     "Content-Type": "application/json",
//     "Content-Length": data.length,
//   },
// };
// https.request((options = options), (data = data));

// const req = https.request(options, (res) => {
//   console.log(`statusCode: ${res.statusCode}`);

//   res.on("data", (d) => {
//     process.stdout.write(d);
//   });
// });

// req.on("error", (error) => {
//   console.error(error);
// });

// req.write(data);
// req.end();

const request = require("request");

request("http://127.0.0.1:8000/api/login", { json: true }, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(body.url);
  console.log(body.explanation);
});
