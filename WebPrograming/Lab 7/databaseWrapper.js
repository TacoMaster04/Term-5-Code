require('dotenv').config();
const mongoose = require("mongoose");

mongoose.connect(`mongodb+srv://${process.env.MONGODB_USERNAME}:${process.env.MONGODB_PASSWORD}@cluster0.3vhsy.mongodb.net/`, {
	/**
	* @deprecated 
	useNewUrlParser: true*/
}).then(() => {
	console.log("Connected to the Database");
}).catch((err) => {
	console.error("An error occured while connecting to the Database", err);
});