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

def raw_request_wrapper(page, data='', method='get'):
    if method == 'get':
        resp = requests.get(API_ENDPOINT + page, auth=(USER, PASS), json=data)
    elif method == 'post':
        resp = requests.post(API_ENDPOINT + page, auth=(USER, PASS), json=data)
    elif method == 'delete':
        resp = requests.post(API_ENDPOINT + page, auth=(USER, PASS), json=data)
    else:
        raise ValueError('method param must be one of "post", "get", or "delete"')

    return json.loads(resp.text)

def find_obj_uuid_by_name(obj_type, obj_name):
    res = raw_request_wrapper('/' + obj_type)['results']
    
    for obj_instance in res:
        if obj_instance['display'] == obj_name:
            return obj_instance['uuid']