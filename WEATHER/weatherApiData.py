import requests

lat = 12.9716
lon = 77.5946

API_KEY = "23d0cd1e29d9413578b60c9a48fd30e3"

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
