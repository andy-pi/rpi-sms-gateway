from flask import Flask, request, Response
from flask_restful import reqparse, Api, Resource
from config import *

app = Flask(__name__)
api = Api(app)

import gammu.smsd
smsd = gammu.smsd.SMSD('/etc/gammu-smsdrc')

parser = reqparse.RequestParser()
parser.add_argument('subject')
parser.add_argument('stripped-text')


def validate(number):
    '''
    Validates whether or not it is a number (currently just checks int)
    '''
    try:
        int(number)
        return number
    except:
        return False

def send_sms(msgbody,number):
    '''
    injects sms into gammu outbox
    '''
    message = {'Text': msgbody, 'SMSC': {'Location': 1}, 'Number': number}
    smsd.InjectSMS([message])


class SendSMSAPI(Resource):
    def post(self):
        args = parser.parse_args()
        unvalidatednumber = args['subject']
        validatednumber=validate(unvalidatednumber)
        if validatednumber is not False:
            msgbody = args['stripped-text'][:160] # get first 160 chars only
            send_sms_t(msgbody,validatednumber)
            return Response(status=202)
            
        else:
            # error handling of invalid number required here
            # for now, enter full international code, 
            # e.g. UK numbers should start +44
            # send mailgun a not accepted/don't rety 406 response
            # https://help.mailgun.com/hc/en-us/articles/202236504-How-do-webhooks-work-
            return Response(status=406)

api.add_resource(SendSMSAPI, '/sendsms/')

if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT ,debug=True)
