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
