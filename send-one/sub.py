# python3.6

import argparse
import random
import time
from paho.mqtt import client as mqtt_client



# CONSTANTS
USERNAME = "akash-sub"
PASSWORD = "pass"

parser = argparse.ArgumentParser()
parser.add_argument('--topic', type=str, required=True)
parser.add_argument('--broker', type=str, required=False, default="localhost")
parser.add_argument('--port', type=int, required=False, default=1883)

args = parser.parse_args()
TOPIC = args.topic
BROKER = args.broker
PORT = args.port

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
print(f"Client-id: {client_id}")

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(TOPIC)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    time.sleep(1)
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
