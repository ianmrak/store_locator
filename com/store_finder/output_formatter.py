import json

def format_output(output, output_type):
    if output_type == 'text':
        return 'The closest store is %s (%s). \nAddress: %s' %(output['store'], output['distance'], output['address'])
    else:
        return json.dumps(output)