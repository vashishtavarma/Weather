import requests

city = "Bangalore"
countryCode = "IN"

API_KEY = "23d0cd1e29d9413578b60c9a48fd30e3"

URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{countryCode}&limit=1&appid={API_KEY}"

request = requests.get(URL)

# Data in JSON format
data = request.json()

# Latitude and longitude
latData = round(data[0]["lat"], 4)
lonData = round(data[0]["lon"], 4)

print(f"latitude: {latData}")
print(f"longitude: {lonData}")
