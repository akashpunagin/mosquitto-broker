# python 3.6

import random
import time
import argparse

from paho.mqtt import client as mqtt_client

# CONSTANTS
USERNAME = "akash"
PASSWORD = "pass"

parser = argparse.ArgumentParser()
parser.add_argument('--topic', type=str, required=True)
parser.add_argument('--msg', type=str, required=True)
parser.add_argument('--broker', type=str, required=False, default="localhost")
parser.add_argument('--port', type=int, required=False, default=1883)

args = parser.parse_args()
TOPIC = args.topic
BROKER = args.broker
PORT = args.port
MESSAGE = args.msg

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
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


def publish(client, msg):
    result = client.publish(TOPIC, msg)
    status = result[0]
    if status == 0:
        print(f"Sent msg:`{msg}` to topic:`{TOPIC}`")
    else:
        print(f"Failed to send message to topic {TOPIC}")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client, MESSAGE)
    time.sleep(1)


if __name__ == '__main__':
    run()