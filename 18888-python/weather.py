import dataclasses
from typing import Optional

import requests
from dataclasses_json import dataclass_json


@dataclass_json
@dataclasses.dataclass
class WeatherInfo:
    city: str
    temperature: int
    feels_like: int
    weather: str
    wind_direction: str
    wind_scale: int
    wind_speed: int
    humidity: int
    pressure: int


class WeatherService:
    # host = "http://localhost:8080"
    host = "http://18888-go:8080"

    @classmethod
    def fetch_city_weather(cls, city_name) -> Optional[WeatherInfo]:
        r = requests.get(cls.host + "/weather_info/" + city_name)
        data = r.json()
        if not data["Weather"]["temp"]:
            return None
        return WeatherInfo(
            city=city_name,
            temperature=int(data["Weather"]["temp"]),
            feels_like=int(data["Weather"]["feelsLike"]),
            weather=data["Weather"]["text"],
            wind_direction=data["Weather"]["windDir"],
            wind_scale=int(data["Weather"]["windScale"]),
            wind_speed=int(data["Weather"]["windSpeed"]),
            humidity=int(data["Weather"]["humidity"]),
            pressure=int(data["Weather"]["pressure"])
        )

    @classmethod
    def fetch_city_weather_multiple_days(cls, city_name):
        api_key = "33ee858476654de99d7c4ec30a5084d2"
        r = requests.get(f"https://geoapi.qweather.com/v2/city/lookup?key={api_key}&location={city_name}&gzip=n")
        city_id = r.json()["location"][0]["id"]
        r = requests.get(f"https://devapi.qweather.com/v7/weather/3d?key={api_key}&location={city_id}&gzip=n&lang=en")
        data = r.json()["daily"]
        pass
