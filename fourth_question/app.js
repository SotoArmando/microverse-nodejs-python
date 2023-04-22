const http = require('http');
const fs = require('fs');
const users_controller = require("./controllers/users/users_controller");
const { application } = require('express');

const hostname = '127.0.0.1';
const port = 3000;


fs.readFile('./public/index.html', function (err, html) {

  if (err) throw err;

  const server = http.createServer((req, res) => {
    res.writeHeader(200, { "Content-Type": "text/html" });
    res.write(html);
    res.end();
  });

  application.use("/users", users_controller);
  
  server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
  });
});



