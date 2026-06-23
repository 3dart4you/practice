# now = dt.datetime.now()
# year = now.year
# if year == 2026:
#     print("Wow!")
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# weekday = now.weekday()
#
# date_of_birth = dt.datetime(year=1989, month=9, day=6, hour=11)
# print(date_of_birth)


import smtplib
import datetime as dt
import random

my_email = "" #рядок нижче все пояснить ;)
password = "" #тут мав би бути пароль, але я замахався з ним розбиратись =)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation!\n\n{quote}"
        )
