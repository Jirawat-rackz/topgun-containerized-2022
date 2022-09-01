package main

import (
	"fmt"
	"os"
	"os/signal"
	"strings"
	"syscall"

	mqtt "github.com/eclipse/paho.mqtt.golang"
	"github.com/jirawat-rackz/topgun-example-subscribers/config"
	"github.com/spf13/viper"
)

func main() {
	initConfig()

	c := make(chan os.Signal, 1)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)

	subClient := mqtt.NewClient(config.MQTTOptions())
	if token := subClient.Connect(); token.Wait() && token.Error() != nil {
		panic(token.Error())
	}

	sub(subClient)
	<-c
}

func sub(client mqtt.Client) {
	topic := viper.GetString("mosquitto.topic")
	token := client.Subscribe(topic, 1, nil)
	token.Wait()
	fmt.Printf("Subscribed to topic: %s", topic)
}

func initConfig() {
	viper.SetConfigName("config-dev") // name of config file (without extension)
	viper.SetConfigType("yml")        // REQUIRED if the config file does not have the extension in the name
	viper.AddConfigPath(".")          // optionally look for config in the working directory
	err := viper.ReadInConfig()       // Find and read the config file
	if err != nil {
		fmt.Printf("Fatal error config file: %s \n", err)
	}

	viper.SetEnvKeyReplacer(strings.NewReplacer(".", "_"))
	viper.AutomaticEnv()
}
