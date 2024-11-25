const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json()); // Parse any requests to JSON data

app.listen(8080, () => {
	console.log("Server is running at port 8080 (http://localhost:8080)");
});

app.get('/', (req, res) => {
	res.send(`
		<li><a href='/status'>/status</a></li>
		<li><a href='/text'>/text</a></li>
		<li><a href='/file'>/file</a></li>
		<li><a href='/object'>/object</a></li>
		<li><a href='/objectarray'>/objectarray</a></li>
		<li><a href='/calc?num1=5&num2=5'>/calc</a></li>
	`);
});

app.get('/status', (req, res) => {
	res.sendStatus(200);
});

app.get('/text', (req, res) => {
	res.send("<h1>Welcome</h1> <p>Text Text Text Text Text Text Text Text Text </p>");
});

app.get('/file', (req, res) => {
	res.sendFile(__dirname + '/index.html');
});

app.get('/object', (req, res) => {
	res.send({ name: "John", age: 30 });
});

app.get('/objectarray', (req, res) => {
	res.send([
		{ id: 1, name: "product 1" },
		{ id: 2, name: "product 2" },
		{ id: 3, name: "product 3" },
	]);
});

app.post('/student', (req, res) => {
	console.log(req.body);
	res.send(req.query);
	res.send({ id: 1, name: "John", age: 30 });
});

app.get('/calc', (req, res) => {
	//http://localhost:8080/calc?num1=5&num2=5
	const num1 = Number(req.query.num1);
	const num2 = Number(req.query.num2);
	const result = num1 + num2;
	res.send({ num1, num2, result });
});