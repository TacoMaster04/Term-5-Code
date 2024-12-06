const express = require('express');
const app = express();
const bodyParser = require('body-parser');

let persons = [
	{
		id: 1, name: 'Arto Hellas', age: 30, cars: [
			{ id: 1, make: 'Toyota', model: 'Corolla' },
			{ id: 2, make: 'Ford', model: 'Fiesta' }]
	},
	{
		id: 2, name: 'Ada Lovelace', age: 31, cars: [
			{ id: 3, make: 'Toyota', model: 'Yaris' }]
	},
	{
		id: 3, name: 'Dan Abramov', age: 32, cars: [
			{ id: 4, make: 'Ford', model: 'Focus', },
			{ id: 5, make: 'Toyota', model: 'Corolla' },]
	}
];

app.use(bodyParser.json());

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/index.html");
});

app.get("/persons", (req, res) => {
	res.send(persons);
});

app.post("/persons", (req, res) => {
	const newPerson = req.body;
	persons.push(newPerson);
	res.status(201).send(newPerson);
});

app.listen(3000, () => {
	console.log("App is listening on port 3000 http://localhost:3000");
});