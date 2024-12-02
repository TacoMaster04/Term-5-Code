const express = require('express');
const bodyParser = require('body-parser');

const app = express();

let students = [
	{ name: "John", address: "Alex" },
	{ name: "Doe", address: "Alex" },
	{ name: "Jane", address: "Alex" },
	{ name: "Smith", address: "Alex" },
	{ name: "Alex", address: "Alex" },
	{ name: "John", address: "Alex" },
	{ name: "Doe", address: "Alex" },
];

app.use(bodyParser.json());

app.listen(3000, () => { console.log("Listening on port 3000"); });

app.get("/students", (req, res) => {
	res.sendFile(__dirname + "/frontend/index.html");
});

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
	res.send({ msg: "ok" });
});

app.post('/student/update', (req, res) => {
	const studentIndex = Number(req.query.index);
	const studentData = req.body;
	students[studentIndex] = studentData;
	res.send({ msg: "ok" });
});

app.get('/student/delete', (req, res) => {
	const studentIndex = Number(req.query.index);
	students.splice(studentIndex, 1);
	res.send({ msg: "ok" });
});