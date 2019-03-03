import paho.mqtt.client as mqtt
import json, os, urllib.parse, dynamodb_store, configparser, mysql_store
# Parse Config File
config = configparser.ConfigParser()
config.read('app.conf')
if config['MAIN'].getboolean('MYSQL_ENABLE'):
    mysql_store.connectdb(config['MYSQL'])
########################## Data Parsing and Processing
def store_data(data):
    ''' Stores data in relevant database'''
    sensor_data = json.loads(data) # Parses MQTT Data from JSON string to Object
    meta = sensor_data['meta']
    PM_sensor = sensor_data['payload']['PM']
    datetime = meta['time'] + " " + meta['date']
    if PM_sensor != 'null':
        PM2_5 = PM_sensor['PM2.5']
        dbg_msg = "PM2.5: " + str(PM2_5)
        if config['MAIN'].getboolean('DYNAMODB_ENABLE'):
            try:
                dynamodb_store.save(meta['device_id'],meta['timestamp'],datetime,PM2_5)
            except Exception as e:
                print('DYNAMODB ERROR')
                print(str(e))

        if config['MAIN'].getboolean('MYSQL_ENABLE'):
            try:
                payload = sensor_data['payload']
                mysql_store.addMeasureTimePoint(meta,payload)
            except Exception as e:
                print('MYSQL ERROR: Failed to add Time Point')
                print(str(e))
    else:
        dbg_msg = "Failed Data"
    return "TS: "+datetime + " Message: " + dbg_msg

##########################Define event callbacks

def on_connect(client, userdata, flags, rc):
    """Handles upon connect to the MQTT Broker"""
    print("Connection: " + mqtt.connack_string(rc))

def on_message(client, obj, msg):
    """Handles when a message is received from MQTT Broker"""
    #print(msg.topic + " QOS:" + str(msg.qos) + " Payload" + str(msg.payload))
    if msg.topic:
        try:
            debug_message = store_data(msg.payload)
            print(debug_message)
        except Exception as e: 
            print ("Data storage has failed")
            print(e)
          

def on_subscribe(client, obj, mid, granted_qos):
    """#Handles when subscription initially takes place."""
    print("Subscribe Complete. Message ID: " + str(mid) + " QOS: " + str(granted_qos))

def on_log(client, obj, level, string):
    """Called when log information is present. For compliance purposes."""
    print(string)

#Create MQTT Client Instance
mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Parse MQTT_URL (or fallback to localhost)
url_str = os.environ.get('MQTT_URL',config['MQTT']['URL'])
url = urllib.parse.urlparse(url_str)

#Subscribed Topics - ('topicname',QOS) - in the tuple
topic_list = [('datastream/#',0),]

# Connect to MQTT Broker
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)
mqttc.subscribe(topic_list)# Start subscription to list of topics.
# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
