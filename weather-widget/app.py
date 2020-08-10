from flask import Flask, request, render_template, abort # noqa
from dotenv import load_dotenv # noqa
import os
import json
import requests # noqa


load_dotenv()
weather_api_key = os.getenv('OPEN_WEATHER_KEY')
maps_api_key = os.getenv('MAPS_API_KEY')
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

f = open("static/city.list.min.json", encoding="utf8")
cities = json.load(f)
f.close()


# Home
@app.route('/')
def home():
    name = request.args.get("name", "World")
    return render_template("index.html", name=name, url=request.url_root)


@app.route('/cities')
def get_city():
    search = request.args.get('city')
    search = search.lower().title()

    if (search):
        results = []

        for city in cities:
            if city.get("name").startswith(search):
                content = (city.get("name") + ", " + city.get("country"))
                results.append('<a href="/city?id=' +
                               str(city.get("id")) + '" ' +
                               'class="list-group-item ' +
                               'list-group-item-action">' +
                               content + '</a>')

        if (results):
            return "<br>".join(map(str, results))

    return "Not found"


@app.route('/city')
def city_weather():
    cityID = int(request.args.get('id'))
    for city in cities:
        if city.get("id") == cityID:
            name = city.get("name")
            country = city.get("country")
            units = "metric"
            url = "http://api.openweathermap.org/data/2.5/weather"

            params = {"id": cityID,
                      "appid": weather_api_key,
                      "units": units
                      }
            response = requests.get(url, params=params).json()

            weather = response.get('weather')[0].get('main')
            description = response.get('weather')[0].get('description')
            icon = response.get('weather')[0].get('icon')
            minimum = response.get('main').get('temp_min')
            maximum = response.get('main').get('temp_min')
            temp = response.get('main').get('temp')
            lat = response.get('coord').get('lat')
            lon = response.get('coord').get('lon')

            if units == "metric":
                un = '°C'

            return render_template("weather.html", city=name, country=country,
                                   weather=weather,
                                   desc=description.capitalize(),
                                   temp=temp, min=minimum,
                                   max=maximum, unit=un, icon=icon,
                                   lat=lat, lon=lon, map_key=maps_api_key)

    abort(404)


if __name__ == '__main__':
    app.run()
