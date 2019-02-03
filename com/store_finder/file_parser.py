import csv

def parse_file(path):
    STORE_INDEX = 0
    ADDRESS_INDEX = 2
    LAT_INDEX = 6
    LONG_INDEX = 7

    with open(path, 'rU') as f:
        reader = csv.reader(f)
        next(reader, None)
        return {rows[STORE_INDEX]: { 'lat': rows[LAT_INDEX], 'lng': rows[LONG_INDEX], 'address': rows[ADDRESS_INDEX] } for rows in reader}