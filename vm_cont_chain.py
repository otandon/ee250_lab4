import time
import paho.mqtt.client as mqtt

BROKER = "172.20.10.10"
PING = "otandon/ping"
PONG = "otandon/pong"

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
    client.subscribe(PING)

def on_message(client, userdata, message):
    num = int(message.payload.decode())
    print(f"Received ping: {num}")
    num += 1
    time.sleep(1)
    print(f"Sending pong: {num}")
    client.publish(PONG, num)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()