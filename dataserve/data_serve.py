import paho.mqtt.client as mqtt
import json
import os, urllib.parse
import dynamodb
# Configure:
#Default MQTT URL
default_url = 'mqtt://bheazjan:Zj8TLcRab1Wt@m13.cloudmqtt.com:12504'
#Subscribed Topics - ('topicname',QOS) - in the tuple
topic_list = [('datastream/#',0),]
########################## Data Parsing and Processing
def data_parsein(data):
    ''' Parses MQTT Data from JSON string to Object'''
    sensor_data = json.loads(data)
    datetime = sensor_data['time'] + sensor_data['date']
    print(datetime)
    
    if 's_d0' in sensor_data:
        PM2_5 = sensor_data['s_d0']
        print(PM2_5)
        dynamodb.save(sensor_data['device_id'],sensor_data['timestamp'],datetime,PM2_5)
    else:
        print("Failed Data")
    return

##########################Define event callbacks

def on_connect(client, userdata, flags, rc):
    """Handles upon connect to the MQTT Broker"""
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    """Handles when a message is received from MQTT Broker"""
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    #str([msg.topic,msg.payload])
    data_parsein(msg.payload)

def on_subscribe(client, obj, mid, granted_qos):
    """#Handles when subscription initially takes place."""
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    """Called when log information is present. For compliance purposes."""
    print(string)

#Create MQTT Client Instance
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Parse CLOUDMQTT_URL (or fallback to localhost)
url_str = os.environ.get('CLOUDMQTT_URL',default_url)
url = urllib.parse.urlparse(url_str)
topic = 'datastream/#'

# Connect to MQTT Broker
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)
mqttc.subscribe(topic_list)# Start subscription to list of topics.
# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
