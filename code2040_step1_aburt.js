var http = require("http");
http.post = require("http-post");
var url = "http://challenge.code2040.org/api/register";
var myAPIToken = '3624f3214a21f60da7488a0716e6eee3';

var dataToPost = {
	'github': 'https://github.com/skinnyal/CODE2040api_challenge2016_aburt',
	'token': myAPIToken
}


var requestResponse = http.post(url,dataToPost, function(response){
	response.on('data', function(data) {
		console.log(data);
	}).setEncoding('utf8');
});
