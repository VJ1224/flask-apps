from flask import Flask, request, render_template, abort
from dotenv import load_dotenv
import os
import json
import requests


load_dotenv()
weather_api_key = os.getenv('OPEN_WEATHER_KEY')
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
def getCity():
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
def cityWeather():
    cityID = int(request.args.get('id'))
    for city in cities:
        if city.get("id") == cityID:
            name = city.get("name")
            country = city.get("country")
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {"id": cityID,
                      "appid": weather_api_key,
                      "units": "metric"
                      }
            response = requests.get(url, params=params)
            print(response.json())
            return render_template("weather.html", city=name, country=country)

    abort(404)


if __name__ == '__main__':
    app.run()
