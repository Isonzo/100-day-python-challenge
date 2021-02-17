import smtplib
import datetime as dt
import random

my_email = "isonzo@gmail.com"
password = "no"

now = dt.datetime.now()

with open("quotes.txt") as file:
    quotes = file.readlines()


today = now.weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if today == 1:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="renato.soverina@gmail.com",
            msg=f"Subject:Tuesday Sent!\n\n{random.choice(quotes)}"
            )
