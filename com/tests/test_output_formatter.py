from com.store_finder.output_formatter import format_output

import unittest

OUTPUT = {'store': u'Test Store', 'address': u'Test Address', 'distance': '1 mi.'}

class OutputFormatterTest(unittest.TestCase):
 
    def test_formats_output_in_text(self):
        expected = u'The closest store is Test Store (1 mi.). \nAddress: Test Address'
        self.assertEqual(format_output(OUTPUT, 'text') , expected)

    def test_formats_output_in_json(self):
        expected = '{"distance": "1 mi.", "store": "Test Store", "address": "Test Address"}'
        self.assertEqual(format_output(OUTPUT, 'json'), expected)


if __name__ == '__main__':
    unittest.main()