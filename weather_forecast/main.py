import requests

API_KEY = "69f04e4613056b159c2761a9d9e664d2"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
LATITUDE = "37.368832"
LONGITUDE = "-122.036346"
EXCLUDE = "current,minutely,daily"

def get_weather(data, i):
    return data["hourly"][i]["weather"][0]["id"]

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": EXCLUDE
}

response = requests.get(ENDPOINT, params=weather_params)
data = response.json()
weather_list = [get_weather(data, i) for i in range(0, 12)]
print(weather_list)




