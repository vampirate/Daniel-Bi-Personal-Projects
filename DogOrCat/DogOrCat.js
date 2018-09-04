//Initialize all the modules and variables
var request = require('request');
var bodyParser = require('body-parser');
var events = require('events');
var bodyHTML = new events.EventEmitter();
var bodyResponse = new events.EventEmitter();
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({
    extended: false
});
var JsonURL = "temp"

//Get the url from Azure Image Identifier.html

//Allow the use of Cross Origin Resource Sharing
app.use(express.static('public'));
app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

//If the method is post
app.post('/getimageurl', urlencodedParser, function (req, res) {
    //Put the response into "response"
    response = {
        "imageurl": req.body.imageurl
    }
    console.log(response);
    //using an eventemitter to pass on the response to jsonurl variable
    bodyHTML.data = response.imageurl;
    bodyHTML.emit('update');

    //using another eventemitter to get the response from azure to display back to Azure Image Identifier.html
    bodyResponse.on('update', function () {
        res.send(bodyResponse.data)
    })
})


app.listen(3001, function () {
    console.log('listening')
});


bodyHTML.on('update', function () {
    //updating the image url
    data = bodyHTML.data;
    //console.log("data is " + data);
    var spawn = require('child_process').spawn,
        py = spawn('python', ['-u', 'cnn.py']);
    //console.log("cnn spawned");
    py.stdout.on('data', function (data) {
        console.log("data out of python is " + data);
        bodyResponse.data = data;
        bodyResponse.emit('update');
        //console.log("updated1 is " + bodyResponse.data)
        process.exit();
    });
    py.stdin.write(data);
    py.stdin.end();
});