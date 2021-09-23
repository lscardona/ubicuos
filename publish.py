import paho.mqtt.publish as publish
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythonbase"]
mycol = mydb["home"]

broker_address = "localhost"
topic = "casa/habitaciones/hab1/luz"
publish.single(topic, "PUBLISH", hostname=broker_address,
client_id='publicador_ejem2.py')