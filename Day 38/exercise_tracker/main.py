import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv("api_keys.env")
# API CONSTANTS
API_KEY = os.getenv("API")
API_ID = os.getenv("ID")
SHEETY_API = os.getenv("SHEETY")

exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

info = {}

info["query"] = input("Tell me what exercises you did: ")
info["gender"] = "male"
info["weight_kg"] = 65
info["height_cm"] = 186
info["age"] = 20

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
response = requests.post(url=exercise_url, json=info, headers=headers)

exercise_data = response.json()

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

header_sheety = {
    'Content-Type': 'application/json'
}


for exercise in exercise_data["exercises"]:
    print(exercise)
    print("\n")
    sheety_data = {"workout": {
        "date": today,
        "time": time,
        "exercise": exercise["name"],
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(
        url=SHEETY_API, json=sheety_data, headers=header_sheety
    )
    print(response)
