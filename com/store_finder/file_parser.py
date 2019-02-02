import csv

def parse_file(path):
    ADDRESS_INDEX = 2
    LAT_INDEX = 6
    LONG_INDEX = 7

    with open(path, 'rU') as f:
        reader = csv.reader(f)
        next(reader, None)
        return {rows[ADDRESS_INDEX]: { 'lat': rows[LAT_INDEX], 'lng': rows[LONG_INDEX]} for rows in reader}