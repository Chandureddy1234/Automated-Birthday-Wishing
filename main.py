import smtplib
import pandas as pd
import datetime as dt
import random

from dotenv import load_dotenv
import os

load_dotenv('Secrets.txt')  # Assuming secrets.txt is in KEY=VALUE format


my_mail = os.getenv("my_mail")
password = os.getenv("password")
host = os.getenv("EMAIL_HOST")
port = os.getenv("EMAIL_PORT")




#get the present current date
now = dt.datetime.now()
#getting today date

today = (now.month, now.day)



birthdays_csv = pd.read_csv("birthdays.csv")
df = pd.DataFrame(birthdays_csv)

#extracting the name,email,month and date from birtdays.csv
birthdays_dict = {(data_row["month"], data_row["day"]): "{},{}".format(data_row["name"], data_row["email"]) for (index, data_row) in birthdays_csv.iterrows()}


if today in birthdays_dict:
    birthdays_dict[today].split(",")
    name = birthdays_dict[today].split(",")[0]
    emaill = birthdays_dict[today].split(",")[1]

    random_num = random.randint(1,4)
    with open(f'letter_templates/letter_{random_num}.txt') as letter_file:
        letter = letter_file.read()
        letter = letter.replace('[NAME]', name)
    print(letter)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=emaill, msg=f"Subject:Happy Birthday\n\n{letter}".encode('utf-8'))





