import unittest
from user_profile import build_profile

class UserProfileTestCase(unittest.TestCase):
    """
    Tests for 'user_profile.py'
    """

    def test_build_profile_basic(self):
        """
        Test building a profile with only first and last name.
        """
        profile = build_profile("albert", "einstein")
        expected_profile = {
            "first_name": "albert",
            "last_name": "einstein"
        }
        self.assertEqual(profile, expected_profile)

    def test_build_profile_with_kwargs(self):
        """
        Test building a profile with first, last name, and additional keyword arguments.
        """
        profile = build_profile("albert", "einstein", location="princeton", field="physics")
        expected_profile = {
            "first_name": "albert",
            "last_name": "einstein",
            "location": "princeton",
            "field": "physics"
        }
        self.assertEqual(profile, expected_profile)

if __name__ == "__main__":
    unittest.main()
