from twilio.rest import Client
from credentials import account_sid, auth_token, twilio_cell
import Class_Objects_SMS
from flask import Flask, request
from twilio import twiml

## This will be the main logic of the sms messaging service.
client = Client(account_sid, auth_token)
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = requst.form['Body']
    inbound_msg_object = SMS_Msg_Request(number, message_body)
    return_msg = inbound_msg_object.check_if_valid_msg()

    resp = twiml.Response()
    resp.message(return_msg)
    return str(resp)

