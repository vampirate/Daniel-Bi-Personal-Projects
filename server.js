const fs = require('fs');
const child_process = require('child_process');


var ImageIdentifierProcess = child_process.spawn('node', ['Image Identifier.js'], ['-pe', 'process.env.PATH']);
ImageIdentifierProcess.stdout.on('data', function (data) {
    console.log('ImageIdentifierProcess stdout: ' + data);
});
ImageIdentifierProcess.stderr.on('data', function (data) {
    console.log('ImageIdentifierProcess stderr: ' + data);
});
ImageIdentifierProcess.on('close', function (code) {
    console.log('ImageIdentifierProcess exited with code ' + code);
});


var DogOrCatProcess = child_process.exec('node DogOrCat/DogOrCat.js');
DogOrCatProcess.stdout.on('data', function (data) {
    console.log('DogOrCatProcess stdout: ' + data);
});
DogOrCatProcess.stderr.on('data', function (data) {
    console.log('DogOrCatProcess stderr: ' + data);
});
DogOrCatProcess.on('close', function (code) {
    console.log('DogOrCatProcess exited with code ' + code);
});




