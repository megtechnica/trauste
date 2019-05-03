import json
import math as Math


def perimeter_of_circle(lat1, long1):
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
    top_left_corner = (max_long, min_lat)
    bottom_left_corner = (min_long, min_lat)
    top_right_corner = (max_long, max_lat)
    bottom_left_corner = (min_long, min_lat)
    
            


        
