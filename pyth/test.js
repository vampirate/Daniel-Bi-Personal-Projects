var spawn = require('child_process').spawn,
    py = spawn('python', ['c.py']),
    data = 5;
    dataString = '';

py.stdout.on('data', function (data) {
    console.log("adding " + data.toString())
    dataString += data.toString();
});
py.stdout.on('end', function () {
    console.log('Sum of numbers=', dataString);
});
py.stdin.write(JSON.stringify(data));
py.stdin.end();