import requests
import os
from dotenv import load_dotenv

load_dotenv()

lat = 12.9716
lon = 77.5946

API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

# Requesting for data
request = requests.get(URL)
data = request.json()

# print(data)
climateData = data["weather"][0]["main"]

# Converting F to C
temperatureData = round(data["main"]["temp"] - 273.15, 2)

print(f"Climate : {climateData}")
print(f"Temperature : {temperatureData}")
