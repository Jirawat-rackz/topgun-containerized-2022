import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS

MQTT_BROKER_URL = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "iot_center"

INFLUX_DB_BUCKET = "iot_center"
INFLUX_DB_URL = "http://localhost:8086"
INFLUX_DB_ORG = "org"
INFLUX_DB_TOKEN = "admin-token"


influx = InfluxDBClient(url=INFLUX_DB_URL, token=INFLUX_DB_TOKEN, org=INFLUX_DB_ORG)
write_api = influx.write_api(write_options=ASYNCHRONOUS)

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL, MQTT_BROKER_PORT, MQTT_KEEPALIVE_INTERVAL)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, message):
    print(message.topic, message.payload)
    write_api.write(INFLUX_DB_BUCKET, INFLUX_DB_ORG, [message.payload.decode("UTF-8")])


mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.loop_forever()
