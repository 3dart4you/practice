#так як відправити повідомлення не вийде я буду коментувати деякі рядки і просто друкувати листа в консолі

import smtplib
from my_data import my_email, password
import pandas
from datetime import datetime
import random
from collections import defaultdict

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = defaultdict(list)
for index, row in data.iterrows():
    birthdays_dict[(row["month"], row["day"])].append(row)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in birthdays_dict:
    for birthday_person in birthdays_dict[today]:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                my_email,
                birthday_person["email"],
                msg=f"Subject: Happy Birthday!\n\n{contents}"
            )