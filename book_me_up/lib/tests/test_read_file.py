import unittest
import os

from lib import read_file


class ReadFileTest(unittest.TestCase):
    """Tests for the ``ReadFile`` class."""

    def setUp(self):
        """Fixure trat creates a file to be used in this test"""
        self.filename = 'my_test_file.csv'
        with open(self.filename, 'w') as test_file:
            test_file.write(
                'PROPERTY_NAME;PROPERTY_TYPE;LOCAL;STAR_RATING;WEEK_PRICE;WEEKEND_PRICE;'
                'LOYALTY_WEEK_PRICE;LOYALTY_WEEKEND_PRICE\n'
                'Orange;HOTEL;MIAMI;4;100;50;50;20\n'
                'Peach;HOTEL;MIAMI;3;200;100;110;80')

        self.test_file = read_file.ReadFile(self.filename)

        self.expected_data = [['PROPERTY_NAME', 'PROPERTY_TYPE', 'LOCAL', 'STAR_RATING', 'WEEK_PRICE', 'WEEKEND_PRICE',
                               'LOYALTY_WEEK_PRICE', 'LOYALTY_WEEKEND_PRICE'],
                              ['Orange', 'HOTEL', 'MIAMI', '4', '100', '50', '50', '20'],
                              ['Peach', 'HOTEL', 'MIAMI', '3', '200', '100', '110', '80']]

    def tearDown(self):
        """Fixure that deletes files used in this test"""
        try:
            os.remove(self.filename, self.test_file, self.expected_data)
        except:
            pass  # tearDown can't actually be sure that the file exists

    def test_get_file_data(self):
        """Test if data read is correct."""
        test_data = self.test_file.get_data()
        self.assertListEqual(test_data, self.expected_data)

    def test_get_filename(self):
        """Test if filename from file read is correct."""
        test_filename = self.test_file.get_filename()
        self.assertEqual(test_filename, self.filename)


if __name__ == '__main__':
    unittest.main()
