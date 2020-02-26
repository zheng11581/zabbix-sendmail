#!/usr/bin/python

import yagmail
import sys

yag = yagmail.SMTP(user='gih-notifier@gih.cn', host='smtp.gih.cn', port=465)
message_args = sys.argv
if len(message_args) != 3:
    exit(1)
message = {
    'to': message_args[1],
    'subject': message_args[2],
    'contents': message_args[3],
}

yag.send(**message)

