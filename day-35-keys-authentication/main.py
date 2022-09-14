import requests
from twilio.rest import Client


api_key = ""

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_parameters = {
    "appid": api_key,
    "lat": 53.904541,
    "lon": 27.561523,
    "exclude": "current,minutely,daily"
}

response = requests.get(endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

weather_hourly = weather_data["hourly"][:12]

will_rain = False

for hour in weather_hourly:
    if hour["weather"][0]["id"] < 700:
        will_rain = True


account_sid = ""
auth_token = ""

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☂️",
                     from_='+13854427057',
                     to='+9999999999'
                 )
    print(message.status)