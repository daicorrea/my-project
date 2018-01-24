import unittest

from .. import date_time


class DateTimeTest(unittest.TestCase):
    """Tests for the ``date_time()`` function."""

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        date_time.verify_weekday('day')

    def test_verify_weekday(self):
        """Fixure that verifies if passed param has really a week day inside the parenthesis"""
        date_type = date_time.verify_weekday('18Mar2009(wed)')
        self.assertEqual(date_type, 'week')

    def test_verify_weekend(self):
        """Fixure that verifies if passed param has really in a weekend inside the parenthesis"""
        date_type = date_time.verify_weekday('28Mar2009(sat)')
        self.assertEqual(date_type, 'weekend')

    def test_verify_date_with_parenthesis(self):
        """Fixure that verifies if passed param has neither a week day nor a weekend inside the parenthesis"""
        date_type = date_time.verify_weekday('28Mar2009(lar)')
        self.assertEqual(date_type, 'error')

    def test_verify_date_without_parenthesis(self):
        """Fixure that verifies if passed param is neither a week day nor a weekend without parenthesis"""
        date_type = date_time.verify_weekday('potato')
        self.assertEqual(date_type, 'error')

    def test_verify_date_without_parenthesis(self):
        """Fixure that verifies if a week day is really not accepted if passed outside the desired format"""
        date_type = date_time.verify_weekday('mon')
        self.assertEqual(date_type, 'error')


if __name__ == '__main__':
    unittest.main()
