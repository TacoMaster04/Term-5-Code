const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const app = express();
const mongoose = require("mongoose");
const Post = require("./models/post");

mongoose.connect('mongodb+srv://mazenaast:Sfv2p5damyWvh7wK@cluster0.3vhsy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
	.then(() => console.log('Connected to the database successfully!'));

app.use(bodyParser.json());
app.use(cors());

app.listen(3000, () => { console.log("Listening to port 3000 (http://localhost:3000)"); });

app.post("/posts", async (req, res) => {
	const post = new Post(req.body);
	await post.save();
	res.status(201).json(post);
});

app.get("/posts", async (req, res) => {
	const posts = await Post.find();
	res.status(200).json(posts);
});

app.get("/posts/:id", async (req, res) => {
	const post = await Post.findById(req.query.id);
	res.status(200).json(post);
});

app.delete("/posts:id", async (req, res) => {
	const post = await Post.findByIdAndDelete(req.query.id);
	res.status(200).json(post);
});