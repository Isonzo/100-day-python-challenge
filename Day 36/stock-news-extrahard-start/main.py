import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv("/home/renatosf/Documents/Code/python_env_var/python_env_vars.env")
ALPHA_KEY = os.getenv("ALPHA_VANTAGE_KEY")
NEWS_KEY = os.getenv("NEWS_KEY")

STOCK = "INTC"
COMPANY_NAME = "Intel"
get_news = True

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_KEY
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

data = response.json()
today = f"{dt.date.today()}"
if dt.date.weekday(dt.date.today()) == 0:
    d = dt.timedelta(days=3)
    last_friday = dt.date.today()-d
    yesterday = f"{last_friday}"
else:
    d = dt.timedelta(days=1)
    a_day_before = dt.date.today()-d
    yesterday = f"{a_day_before}"


close_price = float(data["Time Series (Daily)"][today]["4. close"])
prev_close_price = float(data["Time Series (Daily)"][yesterday]["4. close"])

print(f"Today the market closed with ${round(close_price, 2)} per stock")
print(f"Yesterday it closed with ${round(prev_close_price, 2)} per stock")
change = (close_price/prev_close_price - 1) * 100

print(f"{COMPANY_NAME}'s stock had a change of {round(change, 2)}%")

if abs(change) >= 5:
    print("Get the news!")
    get_news = True

else:
    print("All's ok, for now\n")
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if get_news:
    parameters = {
        "q": "Intel",
        "apiKey": NEWS_KEY,
        "category": "technology",
        "country": "us"
    }

    response = requests.get("https://newsapi.org/v2/top-headlines", params=parameters)
    response.raise_for_status()

    news = response.json()


    for i in range(min(len(news["articles"]), 3)):
        print(news["articles"][i]["title"])


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
