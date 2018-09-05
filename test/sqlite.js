const sqlite3 = require('sqlite3').verbose();

// open the database
let db = new sqlite3.Database('./headphones.db');

let sql = `SELECT * FROM headphones`;

db.all(sql, [], (err, rows) => {
  if (err) {
    throw err;
  }
  rows.forEach((row) => {
    console.log("Manufacture: " + row.Manufacture);
    console.log("Name: " + row.Name);
    console.log("Price: $" + row.Price);
    console.log("Type: " + row.Type + "\n");
  });
});

// close the database connection
db.close();

////////////////////////////////////////////////////////////////////////

var express = require('express');
var app = express();
var path = require('path');

// viewed at http://localhost:8080
app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname + '/Home.html'));
});

app.listen(8080, function () {
  console.log("Started server at port 8080\n")
});