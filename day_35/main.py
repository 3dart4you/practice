import requests
from my_data import api_key, auth_token, account_sid

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
MY_LAT = 48.922634
MY_LONG = 24.711117

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]

will_you_burn = False
if condition_code > 750:
    will_you_burn = True
if will_you_burn:
    print("Burning an umbrella to cover yourself!")
