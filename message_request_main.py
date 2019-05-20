import json
import requests
from credentials import account_sid, auth_token, twilio_cell
from flask import Flask, request
from twilio import twiml
from twilio.rest import Client

client = Client(account_sid, auth_token)
@app.route('/sms', methods=['POST'])
def get_sms():
    number = request.form['From']
    message_body = request.form['Body']
    message_contents = {"number": number,
                        "text": message_body}
    return message_contents

## def send_error_message(return_msg):
    ## pass
    ## send out return error msg through twilio

def find_coords_from_zip_code(zip_code):
    ## This finds the latitude and longitude of the zip code passed from the sms message
    url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&rows=5000&facet=state&facet=timezone&facet=dst&refine.state=CO"
    json_content = requests.get(url).json()
    content = json.dumps(json_content)
    content = json.loads(content)
    content = content["records"]
    data_set = next(filter(lambda r: r['fields']['zip'] == zip_code, content), None)
    return data_set["fields"]["geopoint"]