# find today's national day
import datetime
import csv
# what's today?


def get_today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


# what's the national day for a given day (i.e. today)
def get_national_days():
    today = get_today()
    # today = '2020-06-16'
    nd = []
    with open('national_days.csv',newline='') as csvfile:
        dates = list(csv.reader(csvfile))
        for l in dates:
            if l[2] == today:
                nd.append(l[1])
    return nd


def format_national_days():
    l = get_national_days()
    beg = ["Today is:"] + l
    out = "\n\t".join(beg)
    return out



