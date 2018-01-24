import unittest

from .. import search_property
from src.property import Property


class SearchPropertyTest(unittest.TestCase):
    """Tests for the ``search_property()`` function."""

    def setUp(self):

        """Fixure trat creates a list to be used in this test"""
        self.first_property = Property(
            property_name = 'Orange',
            property_type = 'HOTEL',
            local = 'MIAMI',
            star_rating = 4,
            week_price = 100,
            weekend_price = 50,
            loyalty_week_price = 50,
            loyalty_weekend_price = 20)

    # def tearDown(self):
    #     """Fixure that deletes list used in this test"""
    #     try:
    #         os.remove(self.first_property)
    #     except:
    #         pass  # tearDown can't actually be sure that the property exists

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        # search_property.property_by_price(self.test_quote_list)
        print(self.property1.property_name)


if __name__ == '__main__':
    unittest.main()