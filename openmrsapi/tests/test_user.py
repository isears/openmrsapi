import unittest
import openmrsapi

class TestUser(unittest.TestCase):
    def setUp(self):
        self.created_user_uuids = list()

    def tearDown(self):
        for uuid in self.created_user_uuids:
            openmrsapi.user.remove(uuid)

    def test_create(self):
        new_user = openmrsapi.user.add(
            'openmrsapi-createtest',
            'Openmrsapi123',
            first_name='Openmrsapi',
            last_name='CreateTest',
            role='Organizational: Doctor',
            gender='M'
        )

        assert 'uuid' in new_user
        self.created_user_uuids.append(new_user['uuid'])

    def test_delete(self):
        new_user = openmrsapi.user.add(
            'openmrsapi-deletetest',
            'Openmrsapi123',
            first_name='Openmrsapi',
            last_name='DeleteTest',
            role='Organizational: Doctor',
            gender='M'
        )

        res = openmrsapi.user.remove(new_user['uuid'])
        assert len(res) == 0