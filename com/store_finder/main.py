import sys
import os

from arg_parser import parse_args
from file_parser import parse_file
from distance_calculator import find_closest_store
from output_formatter import format_output
from google_client import GoogleClient
from user_agent import UserAgent

def main():
    key = os.environ.get('API_KEY', None)
    if key is None:
        sys.exit('Please provide an API key provided for lookup [env=API_KEY]')

    args = parse_args(sys.argv[1:])

    print 'Looking for the closest store near the provided address...'
    client = GoogleClient(UserAgent(), key)
    current_location = client.get_coords(args.address)

    closest_store = get_closest_store(current_location)
    
    output = client.get_distance(args.address, closest_store, units=args.units)

    print '...Done!'

    print '=============================================================='
    print format_output(output, args.output)
    print '=============================================================='

def get_closest_store(current_location):
    store_list = parse_file('com/resources/store-locations.csv')
    closest_store = find_closest_store(current_location, store_list)

    if closest_store is None:
        sys.exit('No stores found, something went wrong')

    return closest_store

main()