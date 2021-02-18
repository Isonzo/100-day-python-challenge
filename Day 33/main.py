import requests
import datetime as dt

MY_LAT = -12.046374

MY_LONG = -77.042793

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
#
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

res.raise_for_status()

data = res.json()

now = dt.datetime.now().hour

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
