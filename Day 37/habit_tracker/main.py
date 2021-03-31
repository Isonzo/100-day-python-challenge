import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("/home/renatosf/Documents/Code/python_env_var/python_env_vars.env")
TOKEN = os.getenv("coomer_token")
USERNAME = "coomer"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coom Graph",
    "unit": "cooms",
    "type": "int",
    "color": "momiji",
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

# POST a pixel

coom_endpoint = f"{graph_endpoint}/graph1"
today = datetime.now()
today_str = today.strftime("%Y%m%d")

coom_counter = input("How many times did you coom today?\n")

pixel_config = {
    "date": today_str,
    "quantity": coom_counter,
}

response = requests.post(url=coom_endpoint, json=pixel_config, headers=header)

print("You can see your shame here\nhttps://pixe.la/v1/users/coomer/graphs/graph1")

# PUT a pixel

# coom_update_point = f"{coom_endpoint}/{today_str}"
#
# pixel_update = {
#     "quantity": coom_counter
# }
#
# response = requests.put(url=coom_update_point, json=pixel_update, headers=header)
# print(response.text)
