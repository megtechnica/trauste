import json
import math as Math


def four_corners(lat1, long1):
    """This function is passed the lat and long from the zip code received.  
    Then calculates the difference in degrees between the center and a coordinate
    on the perimeter of the 5 mile circle
    
    Calculation to find the change in latitude:  5miles/3960.0*(180/pi)"""
    change_in_lat = 0.00126262
    """find the radius of a circle around the earth at a given latitude"""
    r = lambda lat1 : 3960*Math.cos(lat1*(Math.pi/180))
    """find the change in longitude from the center to the coordinate on the perimeter of 
    ## a 5 mile circle"""
    change_in_long = lambda r : 5/r*(180/Math.pi)
    min_long = long1 - change_in_long
    max_long = long1 + change_in_long
    min_lat = lat1 - change_in_lat
    max_lat = lat1 + change_in_lat
    """establishes four corners of the square area"""
    top_left_corner = (min_long, max_lat)
    bottom_left_corner = (min_long, min_lat)
    top_right_corner = (max_long, max_lat)
    bottom_left_corner = (max_long, min_lat)
    return top_left_corner, bottom_left_corner, top_right_corner, bottom_right_corner

def get_coordinates_from_zip(passed_zip_code):        
    with open("CO_Zip_Codes.json","w") as zip_codes_json:
        zip_codes = json.load(zip_codes_json)
        for i in zip_codes:
            if passed_zip_code == i["zip"]:
                ## coordinates returned are [longitude, latitude] 
                coords_of_zip = i["coordinates"]
                ## increases counter to track frequency of searches, allowing us to reorganize the json file
                ## based on frequency of hits first.  
                i["counter"] = i["counter"]+1
                return coords_of_zip

coords_of_zip = get_coordinates_from_zip(passed_zip_code)
top_left, bottom_left, top_right, bottom_right = four_corners(coords[0], coords[1])