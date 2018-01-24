import unittest

from src import hotel


class HotelTest(unittest.TestCase):
    """Tests for the ``Hotel`` class."""

    def setUp(self):
        """Fixure that creates a mock of a hotel to be used in this test"""
        self.first_hotel = hotel.Hotel(
            property_name='Party',
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
            os.remove(self.first_hotel)
        except:
            pass  # tearDown can't actually be sure that the item exist

    def test_return_hotel_name(self):
        """Test if the right value is returned for hotel name"""
        expected_value = 'Party'
        self.assertEqual(self.first_hotel.property_name, expected_value)

    def test_return_hotel_type(self):
        """Test if the right value is returned for hotel type"""
        expected_value = 'HOTEL'
        self.assertEqual(self.first_hotel.property_type, expected_value)

    def test_return_hotel_local(self):
        """Test if the right value is returned for hotel's local"""
        expected_value = 'MIAMI'
        self.assertEqual(self.first_hotel.property_local, expected_value)

    def test_return_hotel_star_rating(self):
        """Test if the right value is returned for hotel's star rating"""
        expected_value = 3
        self.assertEqual(self.first_hotel.property_star_rating, expected_value)

    def test_return_hotel_week_price(self):
        """Test if the right value is returned for hotel's week price"""
        expected_value = 120
        self.assertEqual(self.first_hotel.week_price, expected_value)

    def test_return_hotel_weekend_price(self):
        """Test if the right value is returned for hotel's weekend price"""
        expected_value = 100
        self.assertEqual(self.first_hotel.weekend_price, expected_value)

    def test_return_hotel_loyalty_week_price(self):
        """Test if the right value is returned for hotel's loyalty week price"""
        expected_value = 90
        self.assertEqual(self.first_hotel.loyalty_week_price, expected_value)

    def test_return_hotel_loyalty_weekend_price(self):
        """Test if the right value is returned for hotel's loyalty weekend price"""
        expected_value = 90
        self.assertEqual(self.first_hotel.loyalty_weekend_price, expected_value)


if __name__ == '__main__':
    unittest.main()
