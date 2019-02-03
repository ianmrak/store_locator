from com.store_finder.distance_calculator import find_closest_store, find_rough_distance
from com.store_finder.file_parser import parse_file
import sys

import unittest

ORIGIN_LAT = 34.709779
ORIGIN_LNG = -92.62102100000001
DESTINATION_LAT = 37.959237
DESTINATION_LNG = -122.0779761

class DistanceCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.store_list = parse_file('com/tests/test-locations.csv')

    def test_finds_closest_store(self):
        closest_store = find_closest_store({ 'lat': ORIGIN_LAT, 'lng': ORIGIN_LNG }, self.store_list)
        self.assertEqual(closest_store, {'distance': 36.954451979605864, 'address': '4000 McCain Blvd'})

    def test_finds_closest_store_returns_none_if_no_stores(self):
        closest_store = find_closest_store({ 'lat': ORIGIN_LAT, 'lng': ORIGIN_LNG }, {})
        self.assertEqual(closest_store, {'distance': sys.maxint, 'address': None })

    def test_finds_rough_distance_between_coordinates(self):
        distance = find_rough_distance(ORIGIN_LAT, ORIGIN_LNG, DESTINATION_LAT, DESTINATION_LNG)
        self.assertEqual(distance, 2652.7988805913046)

