import smtplib
import datetime as dt
from random import choice

now = dt.datetime.now()

if now.weekday() != 5:
    exit(0)


with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.read()

random_quote = choice(quotes.splitlines())

my_email = "<EMAIL>"
password = "<PASSWORD>"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="sheen.an.goh@gmail.com",
                        msg=f"Subject:Quote of the Week\n\n{random_quote}")
