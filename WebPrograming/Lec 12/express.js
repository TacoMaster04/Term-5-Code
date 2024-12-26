const express = require('express');
const app = express();
const path = require('path');
const fs = require('fs');
const bodyParser = require('body-parser');
const multer = require('multer');
const cors = require('cors');

app.use(bodyParser.json());
app.use(cors());

app.get('/profile', (req, res) => {
	res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/savepicture', upload.single("file"), (req, res) => {
	res.send(req.file);
});

app.get('/getpicture', (req, res) => {

});

app.listen(3000, () => {
	console.log('Server is running on port 3000');
});

const storage = multer.diskStorage({
	destination: (req, file, cb) => {
		cb(null, path.join(__dirname, 'Uploads'));
	},
	filename: (req, file, cb) => {
		cb(null, `${Date.now()}-${file.originalname}`);
	}
});

const upload = multer({
	storage: storage,
	limits: {
		fileSize: 5 * 1024 * 1024 //5MB
	},
	// fileFilter: (req, file, cb) => {
	// }
});