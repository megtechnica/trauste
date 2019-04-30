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
    "location" : [
        ## Longitude and latitude information are stored here
        ("longitude",""),
        ("latitude","")
    ],
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

statuses = {
    "status" : "",
    "username":"",
    "created":""
}

