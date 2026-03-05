##################### Hard Starting Project ######################
import os
from datetime import datetime
import pandas as pd
import smtplib
import random

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("MY_PASSWORD")
data = pd.read_csv("birthdays.csv")

# iterate over the rows in data
for index, row in data.iterrows():
    month = data["month"][index]
    day = data["day"][index]
    # check if there is a birthday today
    if month == datetime.now().month and day == datetime.now().day:
        # get the person's name and email
        NAME = data["name"][index]
        EMAIL = data["email"][index]
        # open a random birthday message template
        letter_no = random.choice(range(1,4))
        print(f"{letter_no}. {NAME}. {EMAIL}")
        with open(f"letter_templates/letter_{letter_no}.txt", "r") as file:
            # get letter template
            template = file.read()
        personal_birthday_message = template.replace("[NAME]", NAME)
        # send the personal birthday message
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Happy Birthday\n\n{personal_birthday_message}"
            )















# alternative code doing the same thing but with a dictionary comprehension
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )
