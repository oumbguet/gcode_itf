var express= require('express');
var body = require('body-parser');
var cors = require('cors');
const { Console } = require('console');
const {spawn} = require('child_process');

var fs = require('fs');
var http = require('http');
const { exit } = require('process');

var app = express();
var secret = 'kr-uRYX#ZL]~@z~Y?B8KD{gHEL[<?';

app.use(cors({
    origin: 'https://localhost',
    credentials: true,
    allowedHeaders: "Origin, X-Requested-With, Content-Type, Accept"
}));
app.use(body.urlencoded({extended: false}));
app.use(body.json());
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "https://localhost");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.header("Access-Control-Allow-Credentials", true);
    next();
});

var httpServer = http.createServer(app);


//////////////
// MOVEMENT //
//////////////

app.post('/move', async(req, res) => {
    var func = req.body.func;
    var X = req.body.X;
    var Y = req.body.Y;
    var Z = req.body.Z;
    var args = ['gcode.py'];
    var python;

    console.log(func);
    console.log(Z);
    args.push(func);
    if (X != undefined)
        args.push(X);
    if (Y != undefined)
        args.push(Y);
    if (Z != undefined)
        args.push(Z);
    console.log(args);
    python = spawn('python', args);
    python.stdout.on('data', function (data) {
        res.send(data.toString());
    });
    python.on('close', (code) => {
        console.log(`closing with code ${code}`);
    })
});

////////////
// LISTEN //
////////////

httpServer.listen(8080);