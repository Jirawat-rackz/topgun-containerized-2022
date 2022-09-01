package config

import (
	"fmt"

	mqtt "github.com/eclipse/paho.mqtt.golang"
	influxdb2 "github.com/influxdata/influxdb-client-go/v2"
	"github.com/spf13/viper"
)

var messagePubHandler mqtt.MessageHandler = func(client mqtt.Client, msg mqtt.Message) {
	db := influxdb2.NewClient(viper.GetString("influxdb.url"), viper.GetString("influxdb.token"))
	// always close client at the end
	defer db.Close()
	writeAPI := db.WriteAPI(viper.GetString("influxdb.organization"), viper.GetString("influxdb.bucket"))

	// write line protocol
	writeAPI.WriteRecord(string(msg.Payload()))
	// Flush writes
	writeAPI.Flush()
	fmt.Printf("Message received: %s\n", msg.Payload())
}

var connectHandler mqtt.OnConnectHandler = func(client mqtt.Client) {
	fmt.Println("Connected")
}

var connectLostHandler mqtt.ConnectionLostHandler = func(client mqtt.Client, err error) {
	fmt.Printf("Connect lost: %v", err)
}
