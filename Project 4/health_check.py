#! /usr/bin/env python3

import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > 80


def check_disk_usage(disk):
    diskusage = shutil.disk_usage(disk)
    free = diskusage.free / diskusage.total * 100
    return free > 20


def check_available_memory():
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


if check_cpu_usage():
    error_message = "CPU usage is over 80%"
elif not check_disk_usage('/'):
    error_message = "Available disk space is lower than 20%"
elif not check_available_memory():
    error_message = "Available memory is less than 500MB"
elif not check_localhost():
    error_message = "hostname ""localhost"" cannot be resolved to 127.0.0.1"
else:
    pass

# send email if any error reported
if __name__ == "__main__":
    try:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
    except NameError:
        pass
