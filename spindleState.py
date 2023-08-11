#!/usr/bin/env python
import hal, time
import paho.mqtt.client as mqtt
import linuxcnc

# Configuration
broker = "192.168.1.204"  # MQTT broker (replace with your broker address)
topic_running = "cnc/running"  # MQTT topic to publish the message to
topic_state = "cnc/state"  # MQTT topic to publish the message to
topic_speed = "cnc/speed"  # MQTT topic to publish the message to
username = "cnc"  # MQTT broker username
password = "p2cnc"  # MQTT broker password
client = mqtt.Client()
#h = hal.component("passthrough2")
#h = hal.get_value("passthrough")

s = linuxcnc.stat()
s.poll()
# to find the loaded tool information it is in tool table index 0
#if s.tool_table[0].id != 0: # a tool is loaded
#    print s.spindle[0]["override_enabled"]
#else:
#    print "no tool loaded"
# Callback triggered when the spindle status changes
def spindle_status_changed():
    if s.spindle[0]["speed"] == 0:
        publish_message()
        client.publish(topic_running, "spindle is not spinning")
        
    else:
        publish_message()
        client.publish(topic_running, "spindle is spinning")
        

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        publish_message()
        client.publish(topic, "Hello world")  # Publish the message
        
    else:
        print("Failed to connect, return code={}".format(rc))
# Callback triggered when the HAL spindle status changes
#def spindle_status_callback(status):
#    spindle_status_changed(status)

def publish_message():
    client.on_connect = on_connect
    client.username_pw_set(username, password)  # Set the MQTT broker username and password
    client.connect(broker, 1883, 60)  # Connect to the MQTT broker
    # Start the MQTT loop


# Keep the script running
while True:
    s.poll()
    spindle_status_changed()
    publish_message
    print s.spindle[0]["speed"]
    if s.state == 1:
        client.publish(topic_state, "still")  # Publish the message
        publish_message
        client.publish(topic_speed, s.spindle[0]["speed"])  # Publish the message
    elif s.state == 2:
        client.publish(topic_state, "running")  # Publish the message
        publish_message
        client.publish(topic_speed, s.spindle[0]["speed"])  # Publish the message
    client.disconnect()
    time.sleep(1)


