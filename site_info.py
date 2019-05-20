## might needs this, might delete later idk.  
import json

## define the key/value pairs for attributes associated with locations

## must define the hours_open variable to instantiate it inside the "hours" 
## key.
hours_open = {
    "day" : {
        "sunday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
        "monday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
        "tuesday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
        "wednesday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
        "thursday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
        "friday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
        "saturday":
        {
            "open": False,
            "time_open":"",
            "time_close":""
        },
    },
    "24Hours" : False,
    "notes": ""
}
## services will provide a list of the services offered by the shelter.
services = {
    "type": ""
}

## this will contain a list of the updates to the quantity of beds by 
## the username.  
statuses = {
    "status" : "",
    "username":"",
    "created":""
}

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
    "latitude": 0,
    "longitude": 0,
    "phone" : "",
    "type" : "",
    "url" : "",
    "isShelter":False,
    "isIntake":False,
    "hasMeals":False,
    "isFood":False,
    "isFamily":False,
    "isPublic":False,
    "isPrivate":False,
    "isChildren":[False,0],
    "isWomen":[False,0],
    "isMen":[False,0],
    "isTrans":[False,0],
    "isVeteran":[False,0],
    "isDayCenter":False,
    "otherLimits":"",
    "hours": [hours_open],
    "services": [services],
    "notes":"",
    "statuses": [statuses]
}

