var Promise = require("bluebird");
var http = require("http");
http.post = require("http-post");
var url = "http://challenge.code2040.org/api/reverse";
var myAPIToken = '3624f3214a21f60da7488a0716e6eee3';
var validateUrl = 'http://challenge.code2040.org/api/reverse/validate';
var infoToken= {
	'token': myAPIToken
}

function result(){ 
	return new Promise(function (resolve){
	var myData = "";
	var requestResponse = http.post(url,infoToken, function(response){
	response.on('data', function(data) {
		myData = data;
		//console.log(myData);
		resolve (data);
	}).setEncoding('utf8');
	response.on("error",function(error){
		console.log(error);
	})
	
    });


})

};

result().then(
function(data){
	console.log(data);
	var myData = data.split('').reverse().join('');
	console.log(myData);
	//console.log(myData);
	
var dataToPost = {
	'string' : myData,
	'token' : myAPIToken
}

var challengeValidate = http.post(validateUrl,dataToPost,function(response){
	response.on("data",function(data){
		console.log(data);
	}).setEncoding("utf8");


})
});

//reverse();
