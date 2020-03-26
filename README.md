This project is for decoding the MQTT messages we receive from feedmqtt and publish it with additional fields.

### Features
The current version subscribes to feedmqtt.local, extracts the sensor id and publishes on the same channel under the topic "tfc_prod/sensor-id".

### Getting Started

## Prerequisites
+ python paho-mqtt
+ Python3

## Running

Once you have updated the required fields in config_local.json, run the following command to start the decoder.

```
python feedmqtt_decoder.py
```

You could see the published messages using a mqtt client like mosquitto.

```
mosquitto_sub -h hostname -u username -P password -u 'tfc_prod/#'
```
