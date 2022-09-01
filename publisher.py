import random
import time
import paho.mqtt.client as mqtt
from faker import Faker

MQTT_BROKER_URL = "localhost"
MQTT_BROKER_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "iot_center"

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER_URL, MQTT_BROKER_PORT, MQTT_KEEPALIVE_INTERVAL)

fake = Faker()
msg_count = 0
while True:
    time.sleep(0.1)
    Lat, Lng = fake.latlng()
    CO2 = random.randint(1, 20000)
    Pressure = random.randint(1, 20000)
    Temperature = random.randint(1, 20000)
    TVOC = random.randint(1, 20000)
    Humidity = random.randint(1, 20000)
    speed_a = random.randint(1, 20000)
    speed_b = random.randint(1, 20000)
    Distance = random.randint(1, 20000)
    x_axis = random.randint(1, 20000)
    y_axis = random.randint(1, 20000)
    z_axis = random.randint(1, 20000)
    msg = f"environment,CO2Sensor=virtual_CO2Sensor,GPSSensor=virtual_GPSSensor,HumiditySensor=virtual_HumiditySensor,PressureSensor=virtual_PressureSensor,TVOCSensor=virtual_TVOCSensor,TemperatureSensor=virtual_TemperatureSensor,speed_a={speed_a},speed_b={speed_b},distance={Distance},x_axis={x_axis},y_axis={y_axis},z_axis={z_axis},clientId=robot_mac CO2={CO2}i,Humidity={Humidity},Lat={Lat},Lon={Lng},Pressure={Pressure},TVOC={TVOC}i,Temperature={Temperature}"

    result = mqttc.publish(MQTT_TOPIC, msg)
    status = result[0]
    if status == 0:
        print(f"`{msg_count}`send `{msg}` to topic `{MQTT_TOPIC}`")
    else:
        print(f"Failed to send message to topic `{MQTT_TOPIC}`")
    msg_count += 1
