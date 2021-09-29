
//var mqtt = require('mqtt');

var http = require("http");
var mqtt = require('mqtt');
var hostMQTT = 'localhost';
var port = 1883;

var topicSubscribe = "casa/+/luz";

var server = http.createServer(function(request,response){

    client.on('connect', function(){

        console.log("Conexion a MQTT");
        client.subscribe(topicSubscribe, function(err){
            console.log("Subscrpción exitosa");
        })
    
    });
    response.end("Suscricion exitosa");
});
server.listen(8060);