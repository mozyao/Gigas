#!/bin/bash
url='http://t.weather.itboy.net/api/weather/city'
new_url="$url/$1"
curl --header "Content-Type:application/json" "$new_url"> response.json
