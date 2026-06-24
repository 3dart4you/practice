#так як відправити повідомлення не вийде я буду коментувати деякі рядки і просто друкувати листа в консолі

import pandas
from datetime import datetime
import random
from collections import defaultdict

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()

data = pandas.read_csv("birthdays.csv")
df = pandas.DataFrame(data)

birthdays_list = df[(df["day"] == now.day) & (df["month"] == now.month)]
person = birthdays_list["name"]

for name in person:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name)
    print(f"{contents}\n\n")