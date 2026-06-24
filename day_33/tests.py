import requests
from datetime import datetime
import smtplib
from my_data import my_email, password
import time

MY_LAT = 48.922634
MY_LONG = 24.711117

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
# просто інфа по курсу
# if response.status_code == 404:
#     raise Exception ("Thet response does not exist.")
# elif response.status_code == 401:
#     raise Exception ("You are not logged in.")

# 2 дістаю координати
    response.raise_for_status()
    data = response.json()

    iss_longitude =float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
#
# iss_position = (longitude, latitude)
# print(iss_position)

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg="Subject:Look Up!\n\nThe ISS is above you in the sky")