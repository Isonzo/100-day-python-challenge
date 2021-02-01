# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_list = data["temp"].to_list()

# average_temp = sum(data_list) / len(data_list)
#
# print(round(average_temp, 2))

# monday = data[data.day == "Monday"]
#
# fahrenheit = (int(monday.temp) * (9/5) + 32)
#
# print(fahrenheit)

# Create a Dataframe from scratch

# data_dict = {
#     "students": ["Mary", "Jonathan", "Agripino"],
#     "scores": [15, 17, 12]
# }
#
# data = pandas.DataFrame(data_dict)
#
# print(data)
#
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_list = data["Primary Fur Color"]

cinnamon = len(data_list[data_list == "Cinnamon"])
gray = len(data_list[data_list == "Gray"])
black = len(data_list[data_list == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black],
}

fur_data = pandas.DataFrame(data_dict)

print(fur_data)
