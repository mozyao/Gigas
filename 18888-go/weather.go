package main

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"os/exec"
)

func fetchWeather(city string) CityWeather {
	output := city + ".json"
	command := exec.Command("/bin/bash", "weather.sh", city, output)
	_ = command.Start()
	_ = command.Wait()
	file, _ := os.Open(output)
	defer file.Close()
	byteValue, _ := ioutil.ReadAll(file)
	var weatherInfo WeatherInfo
	_ = json.Unmarshal([]byte(byteValue), &weatherInfo)
	return CityWeather{City: city, Weather: weatherInfo}
}
