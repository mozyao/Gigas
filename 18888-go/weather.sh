#!/bin/bash

# global variable
API_KEY=33ee858476654de99d7c4ec30a5084d2
CITY_API=https://geoapi.qweather.com/v2/city/lookup
WEATHER_API=https://devapi.qweather.com/v7/weather/now

# user variable
LOCATION=$1
OUTPUT_FILE=$2
echo "City is $LOCATION"

echo 'Request City Information'
CITY_CODE=$(curl -s -G -d "location=$LOCATION" -d 'gzip=n' -d 'lang=en' -d "key=$API_KEY" $CITY_API | jq '.location[0].id')
CITY_CODE=${CITY_CODE//\"/}
echo "City code is $CITY_CODE"

echo 'Request Weather Information'
curl -s -G -d "location=$CITY_CODE" -d 'gzip=n' -d 'lang=en' -d "key=$API_KEY" $WEATHER_API | jq '.now' > "$OUTPUT_FILE"