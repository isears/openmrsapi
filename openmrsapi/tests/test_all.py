import unittest
import openmrsapi


class AllTests(unittest.TestCase):
    def setUp(self):
        self.created_priv_uuids = list()

    def tearDown(self):
        for uuid in self.created_priv_uuids:
            openmrsapi.delete('privilege', uuid)

    def test_get(self):
        users = openmrsapi.get('user')

        for user in users:
            assert 'uuid' in user
            assert 'display' in user
            assert 'links' in user

        names = [u['display'] for u in users]
        assert 'admin' in names
        assert 'clerk' in names
        assert 'doctor' in names
        assert 'nurse' in names

    def test_post(self):
        new_priv = openmrsapi.post('privilege', data={'name': 'openmrsapi-test-please-delete'})
        assert 'uuid' in new_priv
        self.created_priv_uuids.append(new_priv['uuid'])

    def test_delete(self):
        new_priv = openmrsapi.post('privilege', data={'name': 'openmrsapi-test-please-delete'})
        res = openmrsapi.delete('privilege', new_priv['uuid'])
        assert len(res) == 0

    def test_display_to_uuid(self):
        users = openmrsapi.get('user')

        for user in users:
            uuids = openmrsapi.display_to_uuid('user', user['display'])
            assert len(uuids) == 1
            assert uuids[0] == user['uuid']


if __name__ == '__main__':
    unittest.main()