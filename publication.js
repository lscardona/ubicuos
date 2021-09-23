//librerias
var mqtt = require('mqtt');

//Variables MQTT
var hostMQTT = 'localhost';
var port = 1883;
var topic = 'casa/habitacion/luz';
var message = 'encender habitacion';

function pubTopic(topic, msg) {
  clientMQTT = mqtt.connect({ host: hostMQTT, port: port });
  clientMQTT.on('connect', function () {
    if (clientMQTT.connected) {
      var options = {
        retain: false,
        qos: 1,
      };
      clientMQTT.publish(topic, msg, options);
    }
  });
}
pubTopic(topic, message);
