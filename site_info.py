import json

## define the key/value pairs for attributes associated with locations

site_schema = {
    "name": "",
    "Address" : {
        ## Address information is contained here
        "address1":"",
        "address2":"",
        "city":"",
        "state":"",
        "postalCode":""
    },
    "location" : {
        "longitude":"",
        "latitude":""
    },
    "phone" : "",
    "type" : "",
    "url" : "",
    "isShelter":"",
    "isIntake":"",
    "hasMeals":"",
    "isFood":"",
    "isFamily":"",
    "isPublic":"",
    "isPrivate":"",
    "isChildren":"",
    "isWomen":"",
    "isMen":"",
    "isDayCenter":"",
    "otherLimits":"",
    "hours": "",
    "otherServices": "",
    "notes":"",
    "services": ['service_name_here']
}

services = {
    "type": ""
}

hours_open = {
    "day" : ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'],
    "time_open" : "",
    "time_close" : "",
    "24Hours" : False,
    "notes": ""
}

statuses = {
    "status" : "",
    "username":"",
    "created":""
}

