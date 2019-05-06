import requests
import json

passed_zip = '81221'

url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&facet=state&facet=timezone&facet=dst&refine.state=CO"
## url = "https://public.opendatasoft.com/api/records/1.0/search/?dataset=us-zip-code-latitude-and-longitude&q=co&lang=en&rows=5000&facet=state&facet=timezone&facet=dst&refine.state=CO"
json_content = requests.get(url).json()
content = json.dumps(json_content)
content = json.loads(content)
content = content["records"]

result = next(filter(lambda r: r['fields']['zip'] == passed_zip, content), None)
print(result)

