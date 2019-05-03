import json

with open('CO_Zip_Codes.json', 'r') as zip_codes_json:
    raw_data = json.load(zip_codes_json)
    for i in raw_data:
        print(raw_data[i])
        fields = i["fields"]
        geometry = i["geometry"]
        current_record = { "city":fields["city"],
                            "zip":fields["zip"],
                            "coordinates":geometry["coordinates"]
        }
        with open("CO_Zip_Codes2.json","a") as zip_codes_json2:
            json.dumps(current_record, zip_codes_json2)


        
