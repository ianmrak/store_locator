import googlemaps
import sys

class GoogleClient(object):
    def __init__(self, client):
        self._client = client

    def get_coords(self, address):
        result = self._client.geocode(address)
        if result and len(result) >= 1:
            try:
                return result[0]['geometry']['location']
            except Exception:
                sys.exit('Failed to get current location coordinates')
        else:
            sys.exit('Failed to get response with provided address')

    def get_distance(self, origin, destination, units):
        result = self._client.distance_matrix(origin, destination, units=units)
        if result:
            try:
                return {
                    'address': result['destination_addresses'][0],
                    'distance': result['rows'][0]['elements'][0]['distance']['text']
                }
            except Exception:
                sys.exit('Failed to fetch distance')
        else:
            sys.exit("Failed to get response with provided addresses: %s %s" %(origin, destination))

