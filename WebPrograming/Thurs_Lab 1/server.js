const express = require("express");

const app = express();

let posts = [
	{ name: "Post", reviews: 100 },
	{ name: "Post", reviews: 100 },
	{ name: "Post", reviews: 100 },
	{ name: "Post", reviews: 100 },
];

app.listen(3000, () => { console.log("Listening to port 3000 (http://localhost:3000)"); });

app.get("/posts", (req, res) => {
	res.status(200).send(posts);
	// res.send(posts);
});