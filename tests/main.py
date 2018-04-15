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


if __name__ == '__main__':
    unittest.main()