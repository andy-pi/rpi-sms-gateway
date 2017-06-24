import os
#sudo python /home/pi/rpi-sms-gateway/tr.py IN20170624_124709_00_10086_00.txt IN20170624_124709_00_10086_01.txt

def get_message():
    files = [os.path.join(os.path.split(__file__)[0], 'inbox', m) for m in sys.argv[3:]]
    files.sort()  # make sure we get the parts in the right order
    number = re.match(r'^IN\d+_\d+_\d+_(\+?\d+)_\d+\.txt', os.path.split(files[0])[1]).group(1)
    text = ''
    for f in files:
        text += open(f, 'r').read()

    try:
        text = text.decode('UTF-8', 'strict')
    except UnicodeDecodeError:
        text = text.decode('UTF-8', 'replace')
    return number, text



else:
        # parse from message files
        L.info("No data found in environment, parsing from message files...")
        
        if not len(msg_files):
            print >>sys.stderr, "No message found in environment, and no message paths specified"
            print >>sys.stderr, USAGE % sys.argv[0]
            sys.exit(2)
        L.info("Message file paths: %s", msg_files)

    recipient = sys.argv[1]
    country = flag(sys.argv[2]) or sys.argv[2].upper()
    try:
        number, text = get_message(msg_files)
L.info("From %s: %s", number, repr(text))