import json

import requests
import Class_Objects_SMS
from credentials import account_sid, auth_token, twilio_cell
from flask import Flask, request
from twilio import twiml
from twilio.rest import Client

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

def find_zip_code():
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&rows=5000&facet=state&facet=timezone&facet=dst&refine.state=CO"
    json_content = requests.get(url).json()
    content = json.dumps(json_content)
    content = json.loads(content)
    content = content["records"]
    return next(filter(lambda r: r['fields']['zip'] == passed_zip, content), None)