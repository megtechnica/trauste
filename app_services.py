import re
import message_request_main



def check_if_valid(message_contents):
    msg_body = message_contents["text"]
    try:
        msg_result_re = re.split('\s', message_contents)
        zipcode_re = re.match('\d{5}', msg_result_re[0])
        char_re = re.match('[mMwWfFvVtT]', msg_result_re[1])
        if char_re and zipcode_re:
            return msg_result_re
        else:
            ## error message return
            pass
    except IndexError:
        ## error message return
        pass

def find_change_in_long(latitude):
    earth_radius = 3960.0
    degrees_to_radians = math.pi/180
    radians_to_degrees = 180/math.pi
    r = earth_radius * math.cos(latitude*degrees_to_radians)
    return (10/r)*radians_to_degrees

def find_min_max_coords(zip_code):
    ## the coordinates are in the form of a list with [lat, long]
    coordinates = find_coords_from_zip_code(zip_code)
    ## difference in latitude found by taking 10 miles over the earth's radius and then converting the value to degrees of latitude.
    change_in_latitude = ‭0.14468631190172303251716705761138‬
    lat_coord = coordinates[0]
    max_lat = lat_coord + change_in_latitude
    min_lat = lat_cord - change_in_latitude
    max_long = find_change_in_long(max_lat)
    min_long= find_change_in_long(min_long)
    max_coord = [max_lat,max_long]
    min_coord = [min_lat,min_long]
    return {"max_coord":max_coord, 
            "min_coord": min_coord}





