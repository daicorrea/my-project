import unittest

from src import load_data

class LoadDataTest(unittest.TestCase):

    def test_load_data(self):
        load_data = load_data()