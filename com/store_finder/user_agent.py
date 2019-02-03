import requests
import sys

class UserAgent(object):
    def __init__(self):
        pass

    def get(self, url, params):
            response = requests.get(url, params)
            if response.status_code == 200:
                return response.json()
            else:
                sys.exit('Failed to fetch from %s' %(url))
            