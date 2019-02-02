class MockClientSuccess(object):
    def geocode(self, address):
        return [{u'geometry': {u'location_type': u'APPROXIMATE', u'bounds': {u'northeast': {u'lat': 37.959237, u'lng': -122.0779761}, u'southwest': {u'lat': 37.848223, u'lng': -122.203817}}, u'viewport': {u'northeast': {u'lat': 37.959237, u'lng': -122.0779761}, u'southwest': {u'lat': 37.848223, u'lng': -122.203817}}, u'location': {u'lat': 37.8929461, u'lng': -122.1178261}}, u'address_components': [{u'long_name': u'94549', u'types': [u'postal_code'], u'short_name': u'94549'}, {u'long_name': u'Lafayette', u'types': [u'locality', u'political'], u'short_name': u'Lafayette'}, {u'long_name': u'Contra Costa County', u'types': [u'administrative_area_level_2', u'political'], u'short_name': u'Contra Costa County'}, {u'long_name': u'California', u'types': [u'administrative_area_level_1', u'political'], u'short_name': u'CA'}, {u'long_name': u'United States', u'types': [u'country', u'political'], u'short_name': u'US'}], u'place_id': u'ChIJKUnNc6xjhYARvRe9SXpU90E', u'formatted_address': u'Lafayette, CA 94549, USA', u'types': [u'postal_code']}]
    
    def distance_matrix(self, origin, destination, units):
        return {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'9 mins', u'value': 530}, u'distance': {u'text': u'3.8 mi', u'value': 6140}, u'status': u'OK'}]}], u'origin_addresses': [u'Lafayette, CA 94549, USA'], u'destination_addresses': [u'1871 N Main St, Walnut Creek, CA 94596, USA']}

class MockClientFailure(object):
    def geocode(self, address):
        return []

    def distance_matrix(self, origin, destination, units):
        return []

class MockClientInvalid(object):
    def geocode(self, address):
        return [{'invalid': {}}]

    def distance_matrix(self, origin, destination, units):
        return [{'invalid': {}}]
