import requests
import os
from dotenv import load_dotenv

load_dotenv()

city = "Bangalore"
countryCode = "IN"

API_KEY = os.getenv("OPENWEATHER_API_KEY")

URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{countryCode}&limit=1&appid={API_KEY}"

request = requests.get(URL)

# Data in JSON format
data = request.json()

# Latitude and longitude
latData = round(data[0]["lat"], 4)
lonData = round(data[0]["lon"], 4)

print(f"latitude: {latData}")
print(f"longitude: {lonData}")
