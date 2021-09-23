import paho.mqtt.client as mqtt
import time
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pythonbase"]
mycol = mydb["home"]

def on_message(client, userdata, message):

    mydict = {"data": message.payload.decode("utf-8"), "topic": message.topic}

    x = mycol.insert_one(mydict)
    print("message received", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=",message.qos)
    print("message retain flag=", message.retain)

broker_address="localhost"
print("creating a new instance")
client = mqtt.Client("P1")
client.on_message = on_message
print("connecting to broker")
client.connect(broker_address)
client.loop_start()
print("Subscribing to topic","demo/device/client")
client.subscribe("demo/device/client")
time.sleep(40)
client.loop_stop()