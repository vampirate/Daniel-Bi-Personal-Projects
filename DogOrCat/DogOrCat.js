//Initialize all the modules and variables
var request = require('request');
var bodyParser = require('body-parser');
var events = require('events');
var sendToCnnEmitter = new events.EventEmitter();
var receiveFromCnnEmitter = new events.EventEmitter();
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({
    extended: false
});

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
    //using an eventemitter to pass on the response
    sendToCnnEmitter.data = response.imageurl;
    sendToCnnEmitter.emit('update');

    //using another eventemitter to get the response from azure to display back to Azure Image Identifier.html
    receiveFromCnnEmitter.on('update', function () {
        res.send(receiveFromCnnEmitter.data)
    })
})


app.listen(3001, function () {
    console.log("Listening to port 3001")
});


sendToCnnEmitter.on('update', function () {
    //updating the image url
    data = sendToCnnEmitter.data;
    //console.log("data is " + data);
    var spawn = require('child_process').spawn,
        py = spawn('python', ['-u', __dirname + '/cnn.py']);
    
    console.log("CNN spawned");
    py.stdout.on('data', function (data) {
        console.log("CNN replied: " + data);
        receiveFromCnnEmitter.data = data;
        receiveFromCnnEmitter.emit('update');
        process.exit();
    });
    py.stdin.write(data);
    py.stdin.end();
});