import argparse


def parse_args(args):
    parser = argparse.ArgumentParser()
    addressTypes = parser.add_mutually_exclusive_group()
    addressTypes.add_argument('--zip', dest='address', help='Example: \'Main St., USA\'')
    addressTypes.add_argument('--address', dest='address', help='Example: \'123456\'')
    parser.add_argument('--output', default='text', choices=['text', 'json'])
    parser.add_argument('--units', default='imperial', choices=['imperial', 'metric', 'km', 'mi'])
    parsed_args = parser.parse_args(args)
    parsed_args.units = convert_units(parsed_args.units)

    return parsed_args

def convert_units(units):
    return {
        'km': 'metric',
        'mi': 'imperial'
    }.get(units, units) 
