# sample script to show how to send SMS through SMSD

import gammu.smsd

smsd = gammu.smsd.SMSD('/etc/gammu-smsdrc')

message = {'Text': 'ye', 'SMSC': {'Location': 1}, 'Number': 10086}

smsd.InjectSMS([message])