import requests
import os
import json

try:
    API_ENDPOINT = os.environ['OPENMRS_API_ENDPOINT']
    USER = os.environ['OPENMRS_USERNAME']
    PASS = os.environ['OPENMRS_PASSWORD']
except KeyError:
    print("Error importing environment variables")
    raise

if API_ENDPOINT[-1] != '/':
    API_ENDPOINT += '/'


def _meta_request(target, method, data='', results_only=True):
    """
    Defines actions taken before any api call (GET, POST, or DELETE)

    :param target: API target (e.g. user)
    :type target: str
    :param method: HTTP method (must be one of 'get', 'post', or 'delete'
    :type method: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    if method == 'get':
        resp = requests.get(API_ENDPOINT + target, auth=(USER, PASS), json=data)
    elif method == 'post':
        resp = requests.post(API_ENDPOINT + target, auth=(USER, PASS), json=data)
    elif method == 'delete':
        resp = requests.delete(API_ENDPOINT + target, auth=(USER, PASS), json=data)
    else:
        raise ValueError('Method parameter must be one of: get, post, delete')

    if results_only:
        return json.loads(resp.text)['results']
    else:
        return json.loads(resp.text)


def get(target, data='', results_only=True):
    """
    Makes an HTTP GET request to the API

    :param target: API target (e.g. user)
    :type target: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    return _meta_request(API_ENDPOINT + target, 'get', data=data, results_only=results_only)


def post(target, data='', results_only=True):
    """
    Makes an HTTP POST request to the API

    :param target: API target (e.g. user)
    :type target: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    return _meta_request(API_ENDPOINT + target, 'post', data=data, results_only=results_only)


def delete(target, data='', results_only=True):
    """
    Makes an HTTP DELTE request to the API

    :param target: API target (e.g. user)
    :type target: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    return _meta_request(API_ENDPOINT + target, 'delete', data=data, results_only=results_only)


def display_to_uuid(obj_type, display):
    """
    Looks up uuids by display name

    :param obj_type: API target (e.g. user, person, report)
    :type obj_type: str
    :param display: Display attribute
    :type display: str
    :return: All uuids corresponding to the object with the given 'display' attribute
    """
    res = get('/' + obj_type)
    ret = list()
    
    for obj_instance in res:
        if obj_instance['display'] == display:
            ret.append(obj_instance['uuid'])

    return ret
