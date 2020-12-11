from flask import Flask, request, render_template

from weather import WeatherService

app = Flask(__name__, template_folder='templates')


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/hot_city")
def hot_city():
    data_set = []
    for city in ["beijing", "tianjin", "shanghai", "chongqing","hangzhou"]:
        data = WeatherService.fetch_city_weather(city)
        data = list(data.to_dict().values())
        data_set.append(data)
    if request.args.get("sort") == "temperature":
        data_set = sorted(data_set, key=lambda x: x[1])
    elif request.args.get("sort") == "-temperature":
        data_set = sorted(data_set, key=lambda x: -x[1])
    columns = [
        {"title": "City"},
        {"title": "Temperature"},
        {"title": "Feels Like"},
        {"title": "Weather"},
        {"title": "Wind Direction"},
        {"title": "Wind Scale"},
        {"title": "Wind Speed"},
        {"title": "Humidity"},
        {"title": "Pressure"}
    ]
    return render_template("hot_city.html", columns=columns, data_set=data_set)


@app.route("/city_weather")
def city_name():
    city = request.args.get("city_name")
    data = WeatherService.fetch_city_weather(city)
    data = list(data.to_dict().values())
    data_set = [data]
    columns = [
        {"title": "City"},
        {"title": "Temperature"},
        {"title": "Feels Like"},
        {"title": "Weather"},
        {"title": "Wind Direction"},
        {"title": "Wind Scale"},
        {"title": "Wind Speed"},
        {"title": "Humidity"},
        {"title": "Pressure"}
    ]
    return render_template("city_weather.html", columns=columns, data_set=data_set)


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
