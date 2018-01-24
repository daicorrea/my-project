import unittest

from src import property, price_quote


class PriceQuoteTest(unittest.TestCase):
    """Tests for the ``PriceQuote`` class."""

    def setUp(self):
        """Fixure that creates a mock of to be used in this test"""

        self.first_property = property.Property(
            property_name='Boombiramboo',
            property_type='HOTEL',
            local='MIAMI',
            star_rating=3,
            week_price=120,
            weekend_price=100,
            loyalty_week_price=90,
            loyalty_weekend_price=90
        )

        self.property_quoted = price_quote.PriceQuote(self.first_property, 'rewards', ['25jan2018(thur)', ' 26jan2018(fri)', '27jan2018(sat)'])

    def tearDown(self):
        """Fixure that deletes list used in this test"""
        try:
            os.remove(self.first_property, self.property_quoted)
        except:
            pass  # tearDown can't actually be sure that the item exist

    def test_return_quoted_property_name(self):
        """Test if the right value is returned for quoted property name"""
        expected_value = 'Boombiramboo'
        self.assertEqual(self.property_quoted.get_property().property_name, expected_value)

    def test_return_quoted_client_type(self):
        """Test if the right value is returned for client type"""
        expected_value = 'rewards'
        self.assertEqual(self.property_quoted.get_client_type(), expected_value)

    def test_return_quoted_desired_days(self):
        """Test if the right value is returned for list of desired dates"""
        expected_value = ['25jan2018(thur)', ' 26jan2018(fri)', '27jan2018(sat)']
        self.assertEqual(self.property_quoted.get_desired_days(), expected_value)

    def test_return_quoted_final_price(self):
        """Test if the right value is returned for quoted final price of a property"""
        expected_value = 270
        self.assertEqual(self.property_quoted.get_final_price(), expected_value)




if __name__ == '__main__':
    unittest.main()
