import requests
import openmrsapi
import json


def add(
        username,
        password,
        first_name='',
        middle_name='',
        last_name='',
        force_pass_change=False,
        role='',
        gender='',
        provider_account=True,
        person_uuid=''):
    """
    Adds a user, as well as a person for that user if 'person_uuid' not specified

    :param username: A username for the user
    :type username: str
    :param password: A password for the user
    :type password: str
    :param first_name: User's first name (not used if person_uuid specified)
    :type first_name: str
    :param middle_name: User's middle name (not used if person_uuid specified)
    :type middle_name: str
    :param last_name: User's last name (not used if person_uuid specified)
    :type last_name: str
    :param force_pass_change: Whether or not to force a password change on first login
    :type force_pass_change: bool
    :param role: The user's role (must be the name of a valid openmrs role)
    :type role: str
    :param gender: The user's gender (must be one of 'M' or 'F'; other genders not supported in openmrs)
    :type gender: str
    :param provider_account: Whether or not the new account is a provider account
    :type provider_account: bool
    :param person_uuid: UUID of an existing person in the openmrs database
    :type person_uuid: str
    :rtype: dict
    :return: The new user's data (guaranteed to contain uuid)
    """
    pass


def remove(uuid):
    """
    Removes a user as well as the person backing that user

    :param uuid: UUID of user to be removed
    :type uuid: str
    :rtype: dict
    :return: Empty if successful, error information otherwise
    """
    pass