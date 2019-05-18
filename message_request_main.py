import json

import requests
import Class_Objects_SMS
from credentials import account_sid, auth_token, twilio_cell
from flask import Flask, request
from twilio import twiml
from twilio.rest import Client
import re

client = Client(account_sid, auth_token)
@app.route('/sms', methods=['POST'])
def get_sms():
    number = request.form['From']
    message_body = request.form['Body']
    message_contents = {"number": number,
                        "text": message_body}
    return message_contents

def send_error_message()

def find_zip_code(zip_code):
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&rows=5000&facet=state&facet=timezone&facet=dst&refine.state=CO"
    json_content = requests.get(url).json()
    content = json.dumps(json_content)
    content = json.loads(content)
    content = content["records"]
    return next(filter(lambda r: r['fields']['zip'] == passed_zip, content), None)