#!/usr/bin/env python3
import time
import paho.mqtt.client as mqtt

# Configuration
broker = "192.168.1.204"  # MQTT broker (replace with your broker address)
topic = "cnc"  # MQTT topic to publish the message to
username = "cnc"  # MQTT broker username
password = "p2cnc"  # MQTT broker password

# Callback triggered when the spindle status changes
def spindle_status_changed(status):
    if status == "running":
        client.publish(topic, "Spindle is spinning")
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.publish(topic, "Hello, World!")  # Publish the message
        client.disconnect()  # Disconnect from the broker
    else:
        print("Failed to connect, return code={}".format(rc))
# Callback triggered when the HAL spindle status changes
def spindle_status_callback(status):
    spindle_status_changed(status)

# Create MQTT client
#client = mqtt.Client()

# Set username and password
#client.username_pw_set(username, password)

# Connect to MQTT broker
#client.connect(broker, 1883, 60)

client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(username, password)  # Set the MQTT broker username and password

client.connect(broker, 1883, 60)  # Connect to the MQTT broker

#client.loop_forever()  # Start the MQTT client's loop

# Subscribe to HAL spindle status changes
#client.subscribe("motion.spindle-at-speed")

# Set the callback for spindle status changes
#client.message_callback_add("motion.spindle-at-speed", spindle_status_callback)

# Start the MQTT loop
client.loop_start()

# Keep the script running
while True:
    time.sleep(1)


