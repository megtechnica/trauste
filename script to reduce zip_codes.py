import json

with open('CO_Zip_Codes2.json', 'r') as zip_codes_json2:
    raw_data = json.load(zip_codes_json2)
    for i in raw_data:
        fields = i["fields"]
        geometry = i["geometry"]
        current_record = { "city":fields["city"],
                            "zip":fields["zip"],
                            "coordinates":geometry["coordinates"]
        }
        with open("CO_Zip_Codes.json","a") as zip_codes_json:
            json.dump(current_record, zip_codes_json)


        
