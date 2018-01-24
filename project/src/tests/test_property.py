import unittest

from src import property


class PropertyTest(unittest.TestCase):
    """Tests for the ``Property`` class."""

    def setUp(self):
        """Fixure that creates a mock of a property to be used in this test"""
        self.first_property = property.Property(
            property_name='Potato',
            property_type='HOTEL',
            local='MIAMI',
            star_rating=3,
            week_price=120,
            weekend_price=100,
            loyalty_week_price=90,
            loyalty_weekend_price=90
        )

    def tearDown(self):
        """Fixure that deletes list used in this test"""
        try:
            os.remove(self.first_property)
        except:
            pass  # tearDown can't actually be sure that the item exist

    def test_return_property_name(self):
        """Test if the right value is returned for property name"""
        expected_value = 'Potato'
        self.assertEqual(self.first_property.property_name, expected_value)

    def test_return_property_type(self):
        """Test if the right value is returned for property type"""
        expected_value = 'HOTEL'
        self.assertEqual(self.first_property.property_type, expected_value)

    def test_return_property_local(self):
        """Test if the right value is returned for property's local"""
        expected_value = 'MIAMI'
        self.assertEqual(self.first_property.property_local, expected_value)

    def test_return_property_star_rating(self):
        """Test if the right value is returned for property's star rating"""
        expected_value = 3
        self.assertEqual(self.first_property.property_star_rating, expected_value)

    def test_return_property_week_price(self):
        """Test if the right value is returned for property's week price"""
        expected_value = 120
        self.assertEqual(self.first_property.week_price, expected_value)

    def test_return_property_weekend_price(self):
        """Test if the right value is returned for property's weekend price"""
        expected_value = 100
        self.assertEqual(self.first_property.weekend_price, expected_value)

    def test_return_property_loyalty_week_price(self):
        """Test if the right value is returned for property's loyalty week price"""
        expected_value = 90
        self.assertEqual(self.first_property.loyalty_week_price, expected_value)

    def test_return_property_loyalty_weekend_price(self):
        """Test if the right value is returned for property's loyalty weekend price"""
        expected_value = 90
        self.assertEqual(self.first_property.loyalty_weekend_price, expected_value)


if __name__ == '__main__':
    unittest.main()
