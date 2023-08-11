#!/usr/bin/env python3
import time
import paho.mqtt.client as mqtt

# Configuration
broker = "192.168.1.204"  # MQTT broker (replace with your broker address)
topic = "cnc"  # MQTT topic to publish the message to
username = "cnc"  # MQTT broker username
password = "p2cnc"  # MQTT broker password

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.publish(topic, "Hello, World!")  # Publish the message
        client.disconnect()  # Disconnect from the broker
    else:
        print("Failed to connect, return code={}".format(rc))




client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(username, password)  # Set the MQTT broker username and password

client.connect(broker, 1883, 60)  # Connect to the MQTT broker


def publish_mqtt_message():
    client = mqtt.Client()
    client.connect(broker, 1883, 60)
    client.publish(topic, "M3 Command Triggered")
    client.disconnect()

def update_function():
    if hal_gmoccapy.mdi_command == "M3":
        halui.setp('my_mqtt_publisher.trigger_pin', True)
    else:
        halui.setp('my_mqtt_publisher.trigger_pin', False)




# Start the MQTT loop
client.loop_start()

# Keep the script running
while True:
    time.sleep(1)


