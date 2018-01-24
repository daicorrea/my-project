import unittest
import os

from .. import load_data


class LoadDataTest(unittest.TestCase):
    """Tests for the ``load_data()`` function."""

    def setUp(self):
        """Fixure trat creates a file to be used in this test"""
        self.filename = 'my_test_file.csv'
        with open(self.filename, 'w') as test_file:
            test_file.write(
                'PROPERTY_NAME;PROPERTY_TYPE;LOCAL;STAR_RATING;WEEK_PRICE;WEEKEND_PRICE;'
                'LOYALTY_WEEK_PRICE;LOYALTY_WEEKEND_PRICE\n'
                'Orange;HOTEL;MIAMI;4;100;50;50;20\n'
                'Peach;HOTEL;MIAMI;3;200;100;110;80')

    def tearDown(self):
        """Fixure that deletes files used in this test"""
        try:
            os.remove(self.filename)
        except:
            pass  # tearDown can't actually be sure that the file exists

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        load_data.load_database(self.filename)

    def test_validate_file_extension(self):
        """Check if the file extension is correct"""
        check_extension = load_data.validate_file_extension(self.filename, '.csv')
        self.assertTrue(check_extension)

    def test_item_quantity_in_list(self):
        """See if the quantity of columns of test file is right for each line"""
        with open(self.filename, 'rU') as test_file:
            test_data = test_file.readlines()
        for test_line in test_data:
            each_line = test_line.rstrip().split(';')
            self.assertEqual(len(each_line), 8)

    def test_validate_list_quantity(self):
        """Test if the quantity of columns of test file is right using the validate function."""
        with open(self.filename, 'rU') as test_file:
            test_data = test_file.readlines()
        for test_line in test_data:
            each_line = test_line.rstrip().split(';')
            self.assertTrue(load_data.validate_list_quantity(each_line, 8))


if __name__ == '__main__':
    unittest.main()
