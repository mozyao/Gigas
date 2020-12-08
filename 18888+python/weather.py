import json
import os
from dataclasses import dataclass
from typing import Optional, Dict

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class WeatherForecast:
    city_name: str
    date: str
    humidity: int
    pm_25: int
    pm_10: int
    degree: int


class Weather:

    @classmethod
    def load_city_data(cls) -> Dict:
        mapping = {}
        with open("weather.json") as f:
            data = f.read()
        data = json.loads(data)
        for item in data:
            city_code = item["city_code"]
            city_name = item["city_name"]
            mapping[city_name] = city_code
        return mapping

    @classmethod
    def fetch_weather_info(cls, city_name) -> Optional[WeatherForecast]:
        mapping = cls.load_city_data()
        if city_name in mapping:
            city_code = mapping[city_name]
        else:
            city_code = ""
        if not city_code:
            return None
        os.system(f"./weather.sh {city_code}")
        with open("response.json") as f:
            response = f.read()
        response = json.loads(response)
        date = response["date"]
        humidity = response["data"]["shidu"]
        pm_25 = response["data"]["pm25"]
        pm_10 = response["data"]["pm10"]
        degree = response["data"]["wendu"]
        return WeatherForecast(
            city_name=city_name, date=date, humidity=humidity, pm_25=int(pm_25), pm_10=int(pm_10), degree=int(degree)
        )
