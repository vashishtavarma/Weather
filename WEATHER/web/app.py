from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API Key
API_KEY = "23d0cd1e29d9413578b60c9a48fd30e3"


@app.route("/", methods=["GET", "POST"])
def index():
    city = ""
    country_code = ""
    climate = ""
    temperature = ""

    if request.method == "POST":
        city = request.form["city"]
        country_code = request.form["countryCode"]

        # Get latitude and longitude for the given city and country code
        geoUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&limit=1&appid={API_KEY}"
        geoRequest = requests.get(geoUrl)
        geoData = geoRequest.json()

        if geoData:
            lat = round(geoData[0]["lat"], 4)
            lon = round(geoData[0]["lon"], 4)

            # Get weather information using latitude and longitude
            weatherUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
            weatherRequest = requests.get(weatherUrl)
            weatherData = weatherRequest.json()

            climate = weatherData["weather"][0]["main"]
            temperature = round(weatherData["main"]["temp"] - 273.15, 2)
            # Convert Kelvin to Celsius

        else:
            climate = "Invalid city or country code."
            temperature = ""

    return render_template("weather.html", city=city, country_code=country_code, climate=climate,
                           temperature=temperature)


if __name__ == "__main__":
    app.run(debug=True)
