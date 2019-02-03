from com.store_finder.file_parser import parse_file

import unittest

class FileReaderTest(unittest.TestCase):
    def setUp(self):
        self.address_coords = parse_file('com/tests/test-locations.csv')
 
    def test_skips_first_line_header(self):
        no_header = self.address_coords.get('Address', 'NONE')
        self.assertEqual(no_header, 'NONE')

    def test_parses_all_addresses(self):
        self.assertEqual(len(self.address_coords), 3)

    def test_uses_address_key_and_lat_long_values(self):
        self.assertEqual(self.address_coords.get('Crystal'), {'lat': '45.0521539', 'lng': '-93.364854', 'address': '5537 W Broadway Ave'})
        self.assertEqual(self.address_coords.get('Duluth'), {'lat': '46.808614', 'lng': '-92.1681479', 'address': '1902 Miller Trunk Hwy'})
        self.assertEqual(self.address_coords.get('Little Rock North'), {'lat': '34.7893476', 'lng': '-92.2284247', 'address': '4000 McCain Blvd'})
    

if __name__ == '__main__':
    unittest.main()