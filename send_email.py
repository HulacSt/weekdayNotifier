import smtplib, ssl
import datetime
from secrets import pwd

def get_emails(file):
    emailFile = open(file, 'r')
    emails = emailFile.readlines()
    emails = [l.strip('\n\r') for l in emails]
    emailFile.close()
    return(emails)

def send_email(subject, body, recipient):
    port = 465  # For SSL
    # password = input("Type your password and press enter: ")
    password = pwd
    sender = "WeekdayNotifier@gmail.com"
    context = ssl.create_default_context()
    msg = "Subject: " +subject + "\n\n" + body
    msg = "Subject: {subject}\n\n{body}".format(subject = subject, body = body)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        # Send email here
        server.sendmail(sender, recipient, msg)

# get current weekday
def get_weekday():
    nw = datetime.datetime.now()
    return(nw.strftime("%A"))

def weekday_proclamation():
    wd = get_weekday()
    out = []
    s = "It's " + wd + "."
    b = "Happy " + wd + "."
    out.append(s)
    out.append(b)
    return(out)

def email_weekday(recip):
    w = weekday_proclamation()
    for r in recip:
        send_email(subject = w[0],
                   body = w[1],
                   recipient = r)

recips = get_emails('recipients.txt')

email_weekday(recips)

# email_weekday(['hulacst@icloud.com','stevehulac@gmail.com','monwarren@gmail.com'])
# send_email(subject = 'test',body = 'hello',recipient = 'hulacst@icloud.com')
# print(weekday_proclamation())
# send_email(subject = weekday_proclamation(), body = "", recipient = 'hulacst@icloud.com')
