import com.store_finder.arg_parser as arg_parser

import unittest

class ArgParserTest(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_parses_address(self):
        args = arg_parser.parse_args(['--address=Main St.',])
        self.assertEqual(args.address, 'Main St.')

    def test_parses_zip(self):
        args = arg_parser.parse_args(['--zip=12345'])
        self.assertEqual(args.address, '12345')

    def test_exits_when_address_and_zip_provided(self):
        with self.assertRaises(SystemExit) as context:
            arg_parser.parse_args(['--address=Main St.', '--zip=12345'])

    def test_defaults_units_to_imperial(self):
        args = arg_parser.parse_args([])
        self.assertEqual(args.units, 'imperial')

    def test_parses_units_in_imperial(self):
        args = arg_parser.parse_args(['--units=imperial'])
        self.assertEqual(args.units, 'imperial')

    def test_parses_units_in_metric(self):
        args = arg_parser.parse_args(['--units=metric'])
        self.assertEqual(args.units, 'metric')

    def test_converts_km_unit_argument_to_metric(self):
        args = arg_parser.parse_args(['--units=km'])
        self.assertEqual(args.units, 'metric')

    def test_converts_miles_unit_argument_to_imperial(self):
        args = arg_parser.parse_args(['--units=miles'])
        self.assertEqual(args.units, 'imperial')

    def test_exits_when_invalid_units(self):
        with self.assertRaises(SystemExit) as context:
            arg_parser.parse_args(['--units=roman_numeral'])

    def test_defaults_output_to_text(self):
        args = arg_parser.parse_args([])
        self.assertEqual(args.output, 'text')

    def test_outputs_in_text(self):
        args = arg_parser.parse_args(['--output=text'])
        self.assertEqual(args.output, 'text')

    def test_outputs_in_json(self):
        args = arg_parser.parse_args(['--output=json'])
        self.assertEqual(args.output, 'json')

    def test_exits_when_invalid_output(self):
        with self.assertRaises(SystemExit) as context:
            arg_parser.parse_args(['--output=xml'])

if __name__ == '__main__':
    unittest.main()