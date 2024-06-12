import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
SMTP_HOST= os.getenv('SMTP_HOST')
SMTP_PORT= os.getenv('SMTP_PORT')
SMTP_PASSWORD= os.getenv('SMTP_PASSWORD')
SMTP_USERNAME= os.getenv('SMTP_USERNAME')



msg = EmailMessage()
msg['From'] = 'hackerhomah@gmail.com'
msg['To'] = 'animeherna188@gmail.com'
msg['Subject'] = 'Just a Test message'

msg.set_content("HAck vayo hai aba")


with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    # server.sendmail(sender, receiver, message)
    server.send_message(msg)
    