from flask import Flask, jsonify, request

from weather import Weather

app = Flask(__name__)


@app.route("/weather_info")
def weather():
    data = request.json
    city_name = data.get("city_name")
    res = Weather.fetch_weather_info(city_name=city_name)
    if not res:
        return jsonify({})
    else:
        return jsonify(res.to_dict())


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
