const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require('body-parser');
const Customer = require("./model");

const app = express();

app.use(bodyParser.json());
app.listen(8080, () => {
	console.log("App is running on port 8080 (http://localhost:8080)");
});

app.get('/', (req, res) => {
	res.send("Hi");
});

app.post('/customer', async (req, res) => {
	try {
		const newCustomer = new Customer(req.body);
		const savedCustomer = await newCustomer.save();
		res.status(201).json(savedCustomer);
	} catch (err) {
		res.status(400).json({ error: err.message });
	}
});