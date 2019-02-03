import googlemaps
import sys


class GoogleClient(object):
    def __init__(self, user_agent, key):
        self._url = 'https://maps.googleapis.com/maps/api/'
        self._user_agent = user_agent
        self._key = key

    def get(self, uri, params):
        params['key'] = self._key
        return self._user_agent.get(self._url + uri, params)

    def get_coords(self, address):
        result = self.get('geocode/json', {'address': address })
        if result:
            try:
                return result['results'][0]['geometry']['location']
            except Exception:
                sys.exit('Failed to get current location coordinates')
        else:
            sys.exit('Failed to get response with provided address')

    def get_distance(self, origin, closest_store, units):
        params = {'origins': origin, 'destinations': closest_store['address'], 'units': units }
        result = self.get('distancematrix/json', params)
        if result:
            try:
                return {
                    'store': closest_store['store'],
                    'address': result['destination_addresses'][0],
                    'distance': result['rows'][0]['elements'][0]['distance']['text']
                }
            except Exception:
                sys.exit('Failed to fetch distance')
        else:
            sys.exit('Failed to get response with provided addresses: %s %s' %(origin, closest_store['address']))

