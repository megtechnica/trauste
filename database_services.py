import boto3
import json
import decimal
import site_info

dynamodb = boto3.resource('dynamodb', region_name ="us-west2", endpoint_url="http://localhost:8000")

table = dynamodb.Table('Sites')

## Queries the result within the given coordinates to check for available bed counts
def filter_shelters_by_char(response, char):
    filtered_shelters = []
    if m in char:
        for i in response:
            if response["isMen"][0] == True && response["isMen"][1] > 0:
                filtered_shelters.append(response)
    elif w in char:
        for i in response:
            if response["isWomen"][0] == True && response["isWomen"][1] > 0:
                return {"women-beds": response["isWomen"][1]}
    elif f in char:
        for i in response:
            if response["isChildren"][0] == True && response["isChildren"][1] > 0:
                return {"children-beds": response["isChildren"][1]}
    elif t in char:
        for i in response:
            if response["isTrans"][0] == True && response["isTrans"][1] > 0:
                return {"trans-beds": response["isTrans"][1]}
    elif v in char:
        for i in response:
            if response["isVeteran"][0] == True && response["isVeteran"][1] > 0:
                return 
                


## Queries Sites table for shelters within a 10 mile radius.
def query_for_shelters(msg_to_filter):
    max_lat = msg_to_filter["max_coord"][0]
    max_long = msg_to_filter["max_coord"][1]
    min_lat = msg_to_filter["min_coord"][0]
    min_long = msg_to_filter["min_coord"][1]
    char = msg_to_filter["char"]
    response = table.query(KeyConditionExpression=Key('latitude').between(min_lat,max_lat) & Key('longitude').between(min_long, max_long))


