import smtplib
import ssl
import datetime
import secrets
import national_days
import sys
# get the email list from a text file
import argparse


def get_emails():
    parser = argparse.ArgumentParser(description="Select a file with recipient emails")
    parser.add_argument('--file', dest='file', action='store', default="",
                        help="enter a file name to parse")
    args = parser.parse_args()
    emailfile = open(args.file, 'r')
    emails = emailfile.readlines()
    emails = [l.strip('\n\r') for l in emails]
    emailfile.close()
    return emails


def send_email(subject, body, recipient):
    port = 465  # For SSL
    password = secrets.pwd  # from secrets.py
    sender = secrets.un
    context = ssl.create_default_context()
    msg = "Subject: {subject}\n\n{body}".format(subject=subject, body=body)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        # Send email here
        server.sendmail(sender, recipient, msg)


# get current weekday as string
def get_weekday():
    nw = datetime.datetime.now()
    return nw.strftime("%A")


# create weekday proclamation
def weekday_proclamation():
    wd = get_weekday()
    s = "It's " + wd + "."
    if wd == 'Friday':
        b = "Happy " + wd + "!!!"
    else:
        b = "Happy " + wd + "."
    nds = national_days.format_national_days()
    if nds:
        body = nds + "\n\n" + b
    else:
        body = "\n" + b
    out = [s,body]
    return out


# to send the weekday proclamation
def email_weekday(recip):
    w = weekday_proclamation()
    for r in recip:
        send_email(subject=w[0],
                   body=w[1],
                   recipient=r)


recips = get_emails()
email_weekday(recips)