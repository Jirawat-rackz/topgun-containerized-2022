package config

import (
	"fmt"

	mqtt "github.com/eclipse/paho.mqtt.golang"
	"github.com/spf13/viper"
)

func MQTTOptions() *mqtt.ClientOptions {
	host := viper.GetString("mosquitto.host")
	port := viper.GetInt("mosquitto.port")
	options := mqtt.NewClientOptions()
	options.AddBroker(fmt.Sprintf("tcp://%s:%d", host, port))
	options.SetClientID(viper.GetString("mosquitto.clientid"))
	options.SetAutoReconnect(true)
	options.SetDefaultPublishHandler(messagePubHandler)
	options.OnConnect = connectHandler
	options.OnConnectionLost = connectLostHandler
	options.CleanSession = false
	return options
}
