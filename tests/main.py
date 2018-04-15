import unittest
import openmrsapi


class AllTests(unittest.TestCase):
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
        pass

    def test_delete(self):
        pass

    def test_display_to_uuid(self):
        users = openmrsapi.get('user')

        for user in users:
            uuids = openmrsapi.display_to_uuid('user', user['display'])
            assert len(uuids) == 1
            assert uuids[0] == user['uuid']


if __name__ == '__main__':
    unittest.main()