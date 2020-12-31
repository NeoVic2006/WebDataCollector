from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    from_email = 'popalex2020@yandex.ru'
    from_password = 'qwerty123!'
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>." % height

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    server = smtplib.SMTP_SSL('smtp.yandex.com.tr', 465)
    server.ehlo()
    server.starttls()
    server.login(from_email, from_password)
    server.send_message(msg)