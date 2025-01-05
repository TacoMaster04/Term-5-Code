const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
const User = require('./models/userModel');

require('dotenv').config();

const app = express();
app.use(cors());
app.use(bodyParser.json());

mongoose.connect(`mongodb+srv://${process.env.DATABASE_USERNAME}:${process.env.DATABASE_PASSWORD}@cluster0.3vhsy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0`)
	.then(console.log("Connected to the database successfully"));

app.post('/signup', async (req, res) => {
	try {
		const { name, email, password } = req.body;
		if (!name || !email || !password) {
			return res.status(400).json({ message: "Please fill in all fields" });
		}

		const existingUser = await User.findOne({ email });
		if (existingUser) {
			return res.status(420).json({ message: "User already exists" });
		}

		const user = new User({ name, email, password });
		await user.save();
		res.status(201).json({ message: "User created successfully", user: user });
	} catch (er) {
		res.status(500).json({ message: err.message });
	}
});

app.listen(3000, console.log("Server is running on port 3000"));