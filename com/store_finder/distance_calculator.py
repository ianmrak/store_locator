from math import sin, cos, sqrt, atan2, radians
import sys

def find_closest_store(current_location, store_list):
     closest_store = {'address': None, 'distance': sys.maxint}
    
     for address in store_list:
          store_lat = float(store_list[address]['lat'])
          store_lng = float(store_list[address]['lng'])
          distance = find_rough_distance(current_location['lat'], current_location['lng'], store_lat, store_lng)
          if distance < closest_store['distance']:
            closest_store = {'address': address, 'distance': distance}

     return closest_store

# Gets a rough approximation of distance between 2 coordinates
# NOTE: Does not take road travel into account
# Utilizes Haversine formula: https://en.wikipedia.org/wiki/Haversine_formula
def find_rough_distance(lat1, lng1, lat2, lng2):
     radius = 6372.8

     dlat = radians(lat2 - lat1)
     dlon = radians(lng2 - lng1)
     a = (sin(dlat / 2) * sin(dlat / 2) +
          cos(radians(lat1)) * cos(radians(lat2)) *
          sin(dlon / 2) * sin(dlon / 2))
     c = 2 * atan2(sqrt(a), sqrt(1 - a))
     distance = radius * c
     return distance
