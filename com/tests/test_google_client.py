from mock_maps_client import MockClientSuccess, MockClientFailure, MockClientInvalid
from com.store_finder.google_client import GoogleClient

import unittest

ORIGIN = '94549'
DESTINATION = {'store': 'Test Store', 'address': '72223', 'distance': 1 }
UNITS = 'imperial'

class GoogleClientTest(unittest.TestCase):

    def test_gets_lat_lng_from_geocode_result(self):
        client = GoogleClient(MockClientSuccess())
        result = client.get_coords(ORIGIN)
        self.assertEqual(result, {'lat': 37.8929461, 'lng': -122.1178261})

    def test_exits_get_coords_when_response_fails(self):
        client = GoogleClient(MockClientFailure())
        with self.assertRaises(SystemExit) as context:
            client.get_coords(ORIGIN)
    
    def test_exits_get_coords_when_response_invalid(self):
        client = GoogleClient(MockClientInvalid())
        with self.assertRaises(SystemExit) as context:
            client.get_coords(ORIGIN)

    def test_gets_distance_from_matrix_result(self):
        client = GoogleClient(MockClientSuccess())
        result = client.get_distance(ORIGIN, DESTINATION, UNITS)
        self.assertEqual(result, {'address': u'1871 N Main St, Walnut Creek, CA 94596, USA', 'distance': u'3.8 mi', 'store': u'Test Store'})

    def test_exits_get_distance_when_response_fails(self):
        client = GoogleClient(MockClientFailure())
        with self.assertRaises(SystemExit) as context:
            client.get_distance(ORIGIN, DESTINATION, UNITS)

    def test_exits_get_distance_when_response_invalid(self):
        client = GoogleClient(MockClientInvalid())
        with self.assertRaises(SystemExit) as context:
            client.get_distance(ORIGIN, DESTINATION, UNITS)
    

if __name__ == '__main__':
    unittest.main()
