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

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        self.list_quoted_property = []
        self.list_quoted_property.append(PriceQuote(self.test_property_list[0], 'rewards',
                                                    ['23jan2018(tues)', '24jan2018(wed)', '25jan2018(thur)']))
        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        # print(self.best_quoted_property.property_name)

    def test_two_weekdays_one_weekend_price_for_rewards_client(self):
        """Test to see if best hotel returned for 2 week days and 1 weekend day is correct for rewards clients"""
        self.test_data_input_list = ['25jan2018(thur)', ' 26jan2018(fri)', '27jan2018(sat)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'rewards', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Palace')

    def test_two_weekdays_one_weekend_price_for_regular_client(self):
        """Test to see if best hotel returned for 2 week days and 1 weekend day is correct for regular clients"""
        self.test_data_input_list = ['25jan2018(thur)', ' 26jan2018(fri)', '27jan2018(sat)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'regular', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Orange')

    def test_one_weekday_two_weekend_price_for_rewards_client(self):
        """Test to see if best hotel returned for 1 week day and 2 weekend days is correct for rewards clients"""
        self.test_data_input_list = ['26jan2018(fri)', ' 27jan2018(sat)', '28jan2018(sun)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'rewards', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Palace')

    def test_one_weekday_two_weekend_price_for_regular_client(self):
        """Test to see if best hotel returned for 1 week day and 2 weekend days is correct for regular clients"""
        self.test_data_input_list = ['26jan2018(fri)', ' 27jan2018(sat)', '28jan2018(sun)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'regular', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Peach')

    def test_three_weekdays_price_for_regular_client(self):
        """Test to see if best hotel returned for 3 week days is correct for regular clients"""
        self.test_data_input_list = ['25jan2018(wed)', '25jan2018(thur)', ' 26jan2018(fri)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'regular', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Orange')

    def test_three_weekdays_price_for_rewards_client(self):
        """Test to see if best hotel returned for 3 week days is correct for rewards clients"""
        self.test_data_input_list = ['25jan2018(wed)', '25jan2018(thur)', ' 26jan2018(fri)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'rewards', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Orange')

    def test_three_weekend_days_price_for_regular_client(self):
        """Test to see if best hotel returned for 3 weekend days is correct for regular clients"""
        self.test_data_input_list = ['20jan2018(sat)', '27jan2018(sat)', '28jan2018(sun)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'regular', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Peach')

    def test_three_weekend_days_price_for_rewards_client(self):
        """Test to see if best hotel returned for 3 weekend days is correct for rewards clients"""
        self.test_data_input_list = ['20jan2018(sat)', '27jan2018(sat)', '28jan2018(sun)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'rewards', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Palace')

    def test_one_weekend_day_price_for_regular_client(self):
        """Test to see if best hotel returned for 3 weekend days is correct for regular clients"""
        self.test_data_input_list = ['20jan2018(sat)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'regular', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Peach')

    def test_one_weekend_day_price_for_rewards_client(self):
        """Test to see if best hotel returned for 3 weekend days is correct for rewards clients"""
        self.test_data_input_list = ['20jan2018(sat)']

        # Create list of quoted properties passing mocked input data
        self.list_quoted_property = []
        for property in self.test_property_list:
            self.list_quoted_property.append(
                PriceQuote(property, 'rewards', self.test_data_input_list))

        self.best_quoted_property = search_property.property_by_price(self.list_quoted_property)
        self.assertEqual(self.best_quoted_property.property_name, 'Palace')


if __name__ == '__main__':
    unittest.main()
