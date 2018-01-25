import unittest

from .. import search_property
from src.property import Property
from src.price_quote import PriceQuote


class SearchPropertyTest(unittest.TestCase):
    """Tests for the ``search_property()`` function."""

    def setUp(self):
        """Fixure that creates a mock list of properties to be used in this test"""
        self.first_property = Property(
            property_name='Orange',
            property_type='HOTEL',
            local='MIAMI',
            star_rating=3,
            week_price=120,
            weekend_price=100,
            loyalty_week_price=90,
            loyalty_weekend_price=90
        )

        self.second_property = Property(
            property_name='Peach',
            property_type='HOTEL',
            local='MIAMI',
            star_rating=4,
            week_price=170,
            weekend_price=70,
            loyalty_week_price=120,
            loyalty_weekend_price=60
        )

        self.third_property = Property(
            property_name='Palace',
            property_type='HOTEL',
            local='MIAMI',
            star_rating=5,
            week_price=230,
            weekend_price=160,
            loyalty_week_price=110,
            loyalty_weekend_price=50
        )

        # List of properties
        self.test_property_list = [self.first_property, self.second_property, self.third_property]

    def tearDown(self):
        """Fixure that deletes list used in this test"""
        try:
            os.remove(self.first_property, self.second_property, self.third_property, self.test_property_list)
        except:
            pass  # tearDown can't actually be sure that the items exist

    # Function to get the best property using the client type and dates passed by the tests
    def quote_test_property_list(self, client_type, test_data_input_list):
        list_quoted_property = []
        # Create list of quoted properties passing mocked input data
        for property in self.test_property_list:
            list_quoted_property.append(PriceQuote(property, client_type, test_data_input_list))
        best_quoted_property = search_property.property_by_price(list_quoted_property)
        return best_quoted_property

    def test_two_weekdays_one_weekend_price_for_rewards_client(self):
        """Test to see if best hotel returned for two week days and one weekend day is correct for rewards clients"""
        test_data_input_list = ['25jan2018(thur)', ' 26jan2018(fri)', '27jan2018(sat)']
        best_quoted_property = self.quote_test_property_list('rewards', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Palace')

    def test_two_weekdays_one_weekend_price_for_regular_client(self):
        """Test to see if best hotel returned for two week days and one weekend day is correct for regular clients"""
        test_data_input_list = ['25jan2018(thur)', ' 26jan2018(fri)', '27jan2018(sat)']
        best_quoted_property = self.quote_test_property_list('regular', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Orange')

    def test_one_weekday_two_weekend_price_for_rewards_client(self):
        """Test to see if best hotel returned for one week day and two weekend days is correct for rewards clients"""
        test_data_input_list = ['26jan2018(fri)', ' 27jan2018(sat)', '28jan2018(sun)']
        best_quoted_property = self.quote_test_property_list('rewards', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Palace')

    def test_one_weekday_two_weekend_price_for_regular_client(self):
        """Test to see if best hotel returned for one week day and two weekend days is correct for regular clients"""
        test_data_input_list = ['26jan2018(fri)', ' 27jan2018(sat)', '28jan2018(sun)']
        best_quoted_property = self.quote_test_property_list('regular', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Peach')

    def test_three_weekdays_price_for_rewards_client(self):
        """Test to see if best hotel returned for three week days is correct for rewards clients"""
        test_data_input_list = ['25jan2018(wed)', '25jan2018(thur)', ' 26jan2018(fri)']
        best_quoted_property = self.quote_test_property_list('rewards', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Orange')

    def test_three_weekdays_price_for_regular_client(self):
        """Test to see if best hotel returned for three week days is correct for regular clients"""
        test_data_input_list = ['25jan2018(wed)', '25jan2018(thur)', ' 26jan2018(fri)']
        best_quoted_property = self.quote_test_property_list('regular', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Orange')

    def test_three_weekend_days_price_for_rewards_client(self):
        """Test to see if best hotel returned for three weekend days is correct for rewards clients"""
        test_data_input_list = ['20jan2018(sat)', '27jan2018(sat)', '28jan2018(sun)']
        best_quoted_property = self.quote_test_property_list('rewards', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Palace')

    def test_three_weekend_days_price_for_regular_client(self):
        """Test to see if best hotel returned for three weekend days is correct for regular clients"""
        test_data_input_list = ['20jan2018(sat)', '27jan2018(sat)', '28jan2018(sun)']
        best_quoted_property = self.quote_test_property_list('regular', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Peach')

    def test_one_weekend_day_price_for_rewards_client(self):
        """Test to see if best hotel returned for one weekend day is correct for rewards clients"""
        test_data_input_list = ['20jan2018(sat)']
        best_quoted_property = self.quote_test_property_list('rewards', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Palace')

    def test_one_weekend_day_price_for_regular_client(self):
        """Test to see if best hotel returned for one weekend day is correct for regular clients"""
        test_data_input_list = ['20jan2018(sat)']
        best_quoted_property = self.quote_test_property_list('regular', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Peach')

    def test_one_week_day_price_for_rewards_client(self):
        """Test to see if best hotel returned for one week day is correct for rewards clients"""
        test_data_input_list = ['25jan2018(thur)']
        best_quoted_property = self.quote_test_property_list('rewards', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Orange')

    def test_one_week_day_price_for_regular_client(self):
        """Test to see if best hotel returned for one week day is correct for regular clients"""
        test_data_input_list = ['25jan2018(thur)']
        best_quoted_property = self.quote_test_property_list('regular', test_data_input_list)
        # Compare returned value with expected result
        self.assertEqual(best_quoted_property.property_name, 'Orange')


if __name__ == '__main__':
    unittest.main()
