import smtplib, ssl
import datetime
import secrets
import unittest

# get the email list from a text file
def get_emails(file):
    emailFile = open(file, 'r')
    emails = emailFile.readlines()
    emails = [l.strip('\n\r') for l in emails]
    emailFile.close()
    return(emails)


def send_email(subject, body, recipient):
    port = 465  # For SSL
    password = secrets.pwd # from secrets.py
    sender = secrets.un
    context = ssl.create_default_context()
    msg = "Subject: {subject}\n\n{body}".format(subject = subject, body = body)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        # Send email here
        server.sendmail(sender, recipient, msg)

# get current weekday as string
def get_weekday():
    nw = datetime.datetime.now()
    return(nw.strftime("%A"))

# create weekday proclamation
def weekday_proclamation():
    wd = get_weekday()
    out = []
    s = "It's " + wd + "."
    if wd == 'Friday':
        b = "Happy " + wd + "!!!"
    else:
        b = "Happy " + wd + "."
    out.append(s)
    out.append(b)
    return(out)

# to send the weekday proclamation
def email_weekday(recip):
    w = weekday_proclamation()
    for r in recip:
        send_email(subject = w[0],
                   body = w[1],
                   recipient = r)

recips = get_emails('recipients.txt')

email_weekday(recips)
