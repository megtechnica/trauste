import requests
import json
from twilio.rest import Client
from flask import Flask, request

## HTTP_Requests.py imports two libraries that allow for HTTP connections, Flask and Requests.
## Keeping these two libraries in their own module will allow the program to be judicious in 
## it's use of network services.  


## The first url only retrieves 10 records at once.  This line needs to be removed.  
## url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&facet=state&facet=timezone&facet=dst&refine.state=CO"
url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&rows=5000&facet=state&facet=timezone&facet=dst&refine.state=CO"
json_content = requests.get(url).json()
content = json.dumps(json_content)
content = json.loads(content)
content = content["records"]

def find_zip_code(passed_zip, data):
        return next(filter(lambda r: r['fields']['zip'] == passed_zip, content), None)


