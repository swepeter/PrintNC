#!/usr/bin/env python
import time
import threading
import paho.mqtt.client as mqtt
from linuxcnc_hal import HAL

# Configure MQTT parameters
broker_address = "https://192.168.1.204:1883"
broker_port = 1883
username = "cnc"  # MQTT broker username
password = "p2cnc"  # MQTT broker password
topic = "cnc"

# Create an instance of the HAL object
hal = HAL()

# Define the function to publish MQTT messages
def publish_message():
    client = mqtt.Client()
    client.username_pw_set(username, password)  # Set the MQTT broker username and password
    client.connect(broker_address, 1883, 60)  # Connect to the MQTT broker
    #client.connect(broker_address, broker_port)
    client.publish(topic, "M5 command executed")
    client.disconnect()

# Define the callback function for the HAL signal change
def hal_callback(signal_name, signal_value):
    if signal_name == "motion.m5-command" and signal_value:
        # Call the publish_message function when M5 command is executed
        publish_message()

# Set up the HAL signal callback
hal.signal_watch("motion.m5-command", hal_callback)

# Start the HAL thread
hal.start()

# Main loop
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Clean up
hal.stop()
hal.cleanup()

