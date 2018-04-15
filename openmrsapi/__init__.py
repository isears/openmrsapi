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


def _meta_request(resource, method, data='', results_only=True):
    """
    Defines actions taken before any api call (GET, POST, or DELETE)

    :param resource: API resource (e.g. user)
    :type resource: str
    :param method: HTTP method (must be one of 'get', 'post', or 'delete'
    :type method: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    if method == 'get':
        resp = requests.get(API_ENDPOINT + resource, auth=(USER, PASS), json=data)
    elif method == 'post':
        resp = requests.post(API_ENDPOINT + resource, auth=(USER, PASS), json=data)
    elif method == 'delete':
        resp = requests.delete(API_ENDPOINT + resource, auth=(USER, PASS), json=data)
    else:
        raise ValueError('Method parameter must be one of: get, post, delete')

    if resp.status_code == 204:
        return {}
    else:
        ret = json.loads(resp.text)

    if results_only:
        if 'results' in ret:
            return ret['results']
        else:  # API call returned an error
            return ret
    else:
        return ret


def get(resource, data='', results_only=True):
    """
    Makes an HTTP GET request to the API

    :param resource: API resource (e.g. user)
    :type resource: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    return _meta_request(resource, 'get', data=data, results_only=results_only)


def post(resource, data='', results_only=True):
    """
    Makes an HTTP POST request to the API

    :param resource: API resource (e.g. user)
    :type resource: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    return _meta_request(resource, 'post', data=data, results_only=results_only)


def delete(resource, uuid, data='', results_only=True):
    """
    Makes an HTTP DELTE request to the API

    :param resource: API resource (e.g. user)
    :type resource: str
    :param uuid: UUID of resource to be deleted
    :type uuid: str
    :param data: Data payload for request
    :type data: dict
    :param results_only: Whether or not to return metadata along with results
    :type results_only: bool
    :return: Any data returned by API call
    """
    return _meta_request(resource + '/' + uuid, 'delete', data=data, results_only=results_only)


def display_to_uuid(obj_type, display):
    """
    Looks up uuids by display name

    :param obj_type: API resource (e.g. user, person, report)
    :type obj_type: str
    :param display: Display attribute
    :type display: str
    :return: All uuids corresponding to the object with the given 'display' attribute
    """
    res = get(obj_type)
    ret = list()
    
    for obj_instance in res:
        if obj_instance['display'] == display:
            ret.append(obj_instance['uuid'])

    return ret
