import paho.mqtt.client as mqtt
from datetime import datetime, timezone
import json

with open('config_local.json') as json_file:
    config = json.load(json_file)

def get_msg_to_publish(msg):
    sid = msg.topic.split('/')[1]
    ts = str(((datetime.now())
                .replace(tzinfo = timezone.utc))
                .timestamp())

    publish_msg = '{\"acp_id\":\"'+sid+'\", \"acp_ts\": \"'+ts+'\", \"payload\": ' + str(msg.payload.decode("utf-8"))+'}'
    return(sid,publish_msg)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(config['mqttTopic'])

def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    #print(msg.topic)
    sensor_id, pub_msg = get_msg_to_publish(msg)
    topic = 'tfc_prod/'+sensor_id
    #print(topic,pub_msg)
    pubClient = mqtt.Client()
    pubClient.connect('localhost', 1883)
    ret = pubClient.publish(topic, pub_msg)

client = mqtt.Client()
client.username_pw_set(username=config['username'],password=config['password'])
client.on_connect = on_connect
client.on_message = on_message

client.connect(config['hostname'])

client.loop_forever()
