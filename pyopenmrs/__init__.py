#!/usr/bin/env python3

import requests
import os
import json

try:
    API_ENDPOINT = os.environ['OPENMRS_API_ENDPOINT']
    USER = os.environ['OPENMRS_USERNAME']
    PASS = os.environ['OPENMRS_PASSWORD']
except KeyError as e:
    print("Error importing environment variables:")
    print(e)

def raw_request_wrapper(page, data=''):
    resp = requests.get(API_ENDPOINT + page, auth=(USER, PASS), data=data)
    return json.loads(resp.text)