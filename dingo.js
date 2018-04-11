var request = require("request");

var options = { method: 'GET',
    url: 'https://dog.ceo/api/breed/dingo/images/random',
    headers:
        { 'Postman-Token': '780d92bd-0c3d-4395-972f-2915eca5d80c',
            'Cache-Control': 'no-cache' } };

request(options, function (error, response, body) {
    if (error) throw new Error(error);

    console.log(body);
});
