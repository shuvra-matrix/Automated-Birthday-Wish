import smtplib
import datetime as dt
from random import randint
import pandas as pd

date = dt.datetime.now()
data = pd.read_csv("birthdays.csv")
new_data = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

today_date = (date.month, date.day)

my_email = "shuvratcp@gmail.com"
my_password = "iamacool"

random_latter_path = f"letter_templates/letter_{randint(1, 3)}.txt"

if today_date in new_data:
    birthday_boy = new_data[today_date]
    birthday_boy_name = birthday_boy["name"]
    birthday_boy_email = birthday_boy["email"]
    latter_name = "[NAME]"
    with open(f"{random_latter_path}") as file:
        files = file.read()
        new_latter = files.replace(latter_name, birthday_boy_name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as email:
        email.starttls()
        email.login(user=my_email, password=my_password)
        try:
            email.sendmail(from_addr=my_email, to_addrs=birthday_boy_email,
                        msg=f"Subject:Happy Birthday {birthday_boy_name}\n\n{new_latter}")
        except UnicodeEncodeError:
            print("hi")

