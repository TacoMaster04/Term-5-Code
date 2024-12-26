const fs = require('fs');
const path = require('path');

// path.join(__dirname, 'package.json');
// Is the same thing as 
// __dirname + '/package.json';
// path.join(__dirname, 'package.json');
// is used to make the path cross-platform compatible

// fs.existsSync(path)
const doesFileExist = fs.existsSync(path.join(__dirname, 'package.json'));
console.log(doesFileExist);

// fs.writeFileSync(file, content)
fs.writeFileSync(path.join(__dirname, 'test.txt'), 'Hello World');

// fs.readFileSync(path)
const content = fs.readFileSync(path.join(__dirname, 'test.txt'));
console.log(String(content));

// fs.unlinkSync(path)
fs.unlinkSync(path.join(__dirname, 'test.txt')); //Deletes the test.txt file

// fs.appendFileSync(path, content)
fs.appendFileSync(path.join(__dirname, 'new test.txt'), 'Hello World\n'); //Creates a new file and appends the content then adds a new line (\n)

// fs.mkdirSync
fs.mkdirSync(path.join(__dirname, 'Uploads')); //Creates a new folder

// fs.rmdirSync
fs.rmdirSync(path.join(__dirname, 'Uploads')); //Deletes the folder