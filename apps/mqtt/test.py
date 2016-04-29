import paho.mqtt.client as mqtt
from apps.api.models import ContainerReading, Container


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    ny = ContainerReading.objects.create(container=Container.objects.get(id=1), value=msg.payload)
    ny.save()

    # Data is received here and can be stored in the database
    print(msg.topic + " " + str(msg.payload))


def request_depth(client):

    test = {'container': 14, "what": "workwork"}

    print client.publish("ewms/container/request/1", payload="")


def try_connect():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("mqtt.item.ntnu.no", 1883, 60)

    client.subscribe("ewms/container/1")

    counter = 1

    if counter < 5:
        counter += 1
        request_depth(client)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
