#!/usr/bin/env python
#sudo python /home/pi/rpi-sms-gateway/tr.py IN20170624_124709_00_10086_00.txt IN20170624_124709_00_10086_01.txt
from __future__ import print_function
import os, sys, re
from sparkpost import SparkPost
from config import *
sp = SparkPost('SPARKPOST_API_KEY')

def get_message():
    files = [os.path.join('/var/spool/gammu/inbox/', m) for m in sys.argv[1:]]
    files.sort() # make sure we get the parts in the right order
    number = re.match(r'^IN\d+_\d+_\d+_(\+?\d+)_\d+\.txt', os.path.split(files[0])[1]).group(1)
    text = ''
    for f in files:
        text += open(f, 'r').read()
    try:
        text = text.decode('UTF-8', 'strict')
    except UnicodeDecodeError:
        text = text.decode('UTF-8', 'replace')
    return number, text

number, text= get_message()
 
response = sp.transmissions.send(
    use_sandbox=True,
    recipients=['info@andypi.co.uk'],
    html=text,
    from_email='sms.andypi.co.uk',
    subject=number
)