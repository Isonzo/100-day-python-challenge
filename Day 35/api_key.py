import requests
from twilio.rest import Client

account_sid = "AC09a601afbe9fe78bc4179879334f42e1"
auth_token = ""
client = Client(account_sid, auth_token)


parameters = {
    "lat": -0,
    "lon": 52.408989,
    "appid": "your app id (from openweather)",
    "exclude": "current,minutely,daily"
    }


response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall",
    params=parameters
    )

response.raise_for_status()

data = response.json()

not_rain = True

for hour in range(12):
    if data["hourly"][hour]["weather"][0]["id"] < 700 and not_rain:
        message = client.messages \
                .create(
                     body="It's going to rain within the next 12 hours",
                     from_="twilio number",
                     to="your number"
                 )
        not_rain = False
        print(message.status)
