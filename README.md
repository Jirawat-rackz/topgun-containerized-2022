# Topgun Containerized Example

This is an example of how to use **Docker** with **Topgun** Project.

## Requirements
1. Docker Desktop
2. Docker Compose
3. Python
4. Go


## Components
1. Subscribers mqtt with Golang & python
2. Publisher mqtt with Python
3. Mosquitto MQTT Broker
4. InfluxDB
5. Telegraf


## How to run
1. Clone this repository
2. Run `docker compose up -d`
3. Run `pip install -r requirements.txt`
4. Run `python publisher.py` or `python3 publisher.py`
5. `cd subscribers_golang` and run `go run main.go` for Golang subscriber or `python subscriber.py` for python subscriber
6. Open `http://localhost:8086` for InfluxDB 
    - username: admin
    - password: password
7. Open `http://localhost:8000` for Iot_center_v2
8. Register devices with deviceId `robot_mac`

If this works, that mean you can collect the data from the python publisher.