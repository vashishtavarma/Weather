import requests
import os
from dotenv import load_dotenv

load_dotenv()

# OpenWeatherMap API Key
API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter the city: ").title()
countryCode = input("Enter the country code (e.g., IN for India): ").upper()

# Latitude and longitude for the given city and country code
geoUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{countryCode}&limit=1&appid={API_KEY}"
geoRequest = requests.get(geoUrl)
geoData = geoRequest.json()

if not geoData:
    print("Invalid city or country code. Please try again.")
else:
    lat = round(geoData[0]["lat"], 4)
    lon = round(geoData[0]["lon"], 4)

    # Weather information using latitude and longitude
    weatherUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    weatherRequest = requests.get(weatherUrl)
    weatherData = weatherRequest.json()

    climate = weatherData["weather"][0]["main"]
    # Convert Kelvin to Celsius
    temperature = round(weatherData["main"]["temp"] - 273.15, 2)

    print(f"City: {city}, Country: {countryCode}")
    print(f"Latitude: {lat}, Longitude: {lon}")
    print(f"Climate: {climate}")
    print(f"Temperature: {temperature}°C")
