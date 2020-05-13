# weekdayNotifier

Sends an e-mail to selected recipients with the current weekday.

Useful to pair with crontab, etc for running on a schedule (e.g. every day)

The recipient e-mails should be stored in a plaintext file separated by newlines

Store your sending e-mail and password in a separate secrets.py file

To run in crontab us `crontab -e` and add something like this:

`0 9 * * * /home/pi/.pyenv/shims/python /opt/scripts/weekdayNotifier/send_email.py --file /opt/scripts/weekdayNotifier/recipients.txt`

(The script needs to be in /opt/ rather than somewhere in your home folder.)
