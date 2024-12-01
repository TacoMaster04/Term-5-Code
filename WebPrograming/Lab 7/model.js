const mongoose = require("mongoose");

module.exports = mongoose.model("customer", {
	customerId: {
		type: Number
	},
	customerName: {
		type: String
	},
	customerDateOfBirth: {
		type: Date
	},
});

