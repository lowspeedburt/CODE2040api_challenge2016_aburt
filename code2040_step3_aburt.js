
var Promise = require("bluebird");
var http = require("http");
http.post = require("http-post");
var url = "http://challenge.code2040.org/api/haystack";
var myAPIToken = '3624f3214a21f60da7488a0716e6eee3';
var validateUrl = "http://challenge.code2040.org/api/haystack/validate";
var infoToken= {
	'token': myAPIToken
}

function result(){ 
	return new Promise(function (resolve){
		var requestResponse = http.post(url,infoToken, function(response){
			response.on('data', function(data) {
				resolve (data);
			}).setEncoding('utf8');
			response.on("error",function(error){
				console.log(error);
			})
		});
	})
};

result().then(function(data){
	console.log(data);
	data = JSON.parse(data);
	var needle = data["needle"];
	var haystack = data["haystack"];
	console.log(needle);
	console.log(haystack);
	var foundNeedle = haystack.indexOf(needle);
	console.log(foundNeedle);


	var dataToPost = {
		'token': myAPIToken,
		'needle': foundNeedle

	};
	http.post(validateUrl,dataToPost,function(response){
		response.on("data", function(data){
			console.log(data);
		}).setEncoding("utf8");
	});

});
