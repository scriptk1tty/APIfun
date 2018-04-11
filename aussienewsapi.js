var http = require("https");

var options = {
    "method": "GET",
    "hostname": "newsapi.org",
    "port": null,
    "path": "/v2/top-headlines?country=au&apiKey=1594a48417854239bcdbd0d01fb5d86d",
    "headers": {
        "cache-control": "no-cache",
        "postman-token": "05114e36-fb51-06d7-eb5d-0d8440099e0e"
    }
};

var req = http.request(options, function (res) {
    var chunks = [];

    res.on("data", function (chunk) {
        chunks.push(chunk);
    });

    res.on("end", function () {
        var body = Buffer.concat(chunks);
        console.log(body.toString());
    });
});

req.end();