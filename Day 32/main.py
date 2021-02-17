
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "isonzo@gmail.com"
password = "not_going_to_put_my_password"

# Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

data = pd.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")



now = dt.datetime.now()

# 2. Check if today matches a birthday in the birthdays.csv
for birthday in birthdays:
    if now.month == birthday["month"] and now.day == birthday["day"]:
        num = random.randint(1, 3)
        directory = f"letter_templates/letter_{num}.txt"

        with open(directory) as f:
            pre_letter = f.read()

        letter = pre_letter.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday["email"],
            msg=f"Subject:Happy Birthday!\n\n{letter}"
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
