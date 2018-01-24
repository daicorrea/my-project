import unittest

from .. import validate


class LoadDataTest(unittest.TestCase):
    """Tests for the ``text_analyzer()`` function."""

    # Input tests
    def test_user_input_three_dates(self):
        """Test to validate if inputted data has at least one colon and accepts more dates"""
        test_input = validate.validate_user_input('Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)')
        self.assertTrue(test_input)

    def test_user_input_one_date(self):
        """Test to validate if inputted data has at least one colon and accepts only one date"""
        test_input = validate.validate_user_input('Regular: 16Mar2009(mon)')
        self.assertTrue(test_input)

    def test_user_input_four_dates(self):
        """Test to validate if inputted data has at least one colon and accepts four date"""
        test_input = validate.validate_user_input('Regular: 16Mar2009(mon), 17Mar2009(tues), '
                                                  '18Mar2009(wed), 19Mar2009(thur)')
        self.assertTrue(test_input)

    # Client type tests
    def test_user_input_no_date(self):
        """Test to validate if inputted data has no date"""
        test_input = validate.validate_user_input('Regular')
        self.assertFalse(test_input)

    def test_client_type_regular(self):
        """Test to validate if param passed regular is accepted"""
        test_input = validate.validate_client_type('regular')
        self.assertTrue(test_input)

    def test_client_type_rewards(self):
        """Test to validate if param passed rewards is accepted"""
        test_input = validate.validate_client_type('rewards')
        self.assertTrue(test_input)

    def test_client_type_another(self):
        """Test to validate if param passed that is not rewards nor regular is not accepted"""
        test_input = validate.validate_client_type('potato')
        self.assertFalse(test_input)

    # Verify list tests
    def test_validate_empty_list(self):
        """Test to validate if list in the param returns false if empty"""
        test_valid_list = validate.validate_full_list([])
        self.assertFalse(test_valid_list)

    def test_validate_full_list(self):
        """Test to validate if list in the param returns true if it's not empty"""
        test_valid_list = validate.validate_full_list(['potato'])
        self.assertTrue(test_valid_list)


if __name__ == '__main__':
    unittest.main()
