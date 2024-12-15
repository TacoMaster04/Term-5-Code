const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const mongoose = require("mongoose");
const Post = require("./models/Post");

const app = express();

app.use(bodyParser.json());

app.use(cors());

mongoose
  .connect("mongodb+srv://mohamed154:mohamed154@cluster0.otrve.mongodb.net/")
  .then(() => console.log("Connected!"));

app.post("/post", async (req, res) => {
  const post = new Post(req.body);
  await post.save();
  res.status(201).json(post);
});

app.get("/post", async (req, res) => {
  const posts = await Post.find();
  res.status(200).json(posts);
});

app.get("/post/:id", async (req, res) => {
  const posts = await Post.findById(req.params.id);
  res.status(200).json(posts);
});

app.delete("/post/:id", async (req, res) => {
  const posts = await Post.findByIdAndDelete(req.params.id);
  res.status(200).json(posts);
});

app.put("/post/:id", async (req, res) => {
  const posts = await Post.findByIdAndUpdate(req.params.id, req.body, {
    new: true,
  });
  res.status(200).json(posts);
});

app.listen(3000, console.log("server is running"));
