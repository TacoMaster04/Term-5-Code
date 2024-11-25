const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.listen(3099);

let students = [
	{ name: "John", address: "Alex" },
	{ name: "Doe", address: "Alex" },
	{ name: "Jane", address: "Alex" },
	{ name: "Smith", address: "Alex" },
	{ name: "Alex", address: "Alex" },
	{ name: "John", address: "Alex" },
	{ name: "Doe", address: "Alex" },
];

app.get('/student/readall', (req, res) => {
	res.send(students);
});

app.get('/student/read', (req, res) => {
	const studentIndex = req.query.index;
	const student = students[studentIndex];
	if (student) {
		res.send(student);
	} else {
		res.sendStatus(404);
	}
});

app.post('/student/create', (req, res) => {
	const studentBody = req.body;
	students.push(studentBody);
	res.send(200);
});

app.post('/student/update', (req, res) => {

});

app.get('/student/delete', (req, res) => {

});