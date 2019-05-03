import json
import math as Math

def degrees_to_radians(degrees):
    return degrees * Math.PI / 180

def perimeter_of_circle(lat1, long1):
    """This function is passed the lat and long from the zip code received.  
    Then calculates the difference in degrees between the center and a coordinate
    on the perimeter of the 5 mile circle
    
    Calculation to find the change in latitude:  5miles/3960.0*(180/pi)"""
    change_in_lat = 0.00126262
    ## 
    ## find the radius of a circle around the earth at a given latitude
    r = lambda lat1 : 3960*Math.cos(lat1*(Math.pi/180))
    ## find the change in longitude from the center to the coordinate on the perimeter of 
    ## a 5 mile circle
    change_in_long = lambda r : 5/r*(180/Math.pi)
    
            


        
