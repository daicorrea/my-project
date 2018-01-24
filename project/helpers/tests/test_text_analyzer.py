import unittest

from .. import text_analyzer


class LoadDataTest(unittest.TestCase):
    """Tests for the ``text_analyzer()`` function."""

    def test_split_right_text(self):
        """See if the text format passes for a text with both colon and comma"""
        expected_splitted_text = ['Rewards', '26Mar2009(thur)', '27Mar2009(fri)', '28Mar2009(sat)']
        splitted_text = text_analyzer.split_text('Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)')
        self.assertListEqual(expected_splitted_text, splitted_text)

    def test_split_text_without_comma_and_colon(self):
        """See if the text format passes for a text without colon and comma in only one string"""
        expected_splitted_text = ['Rewards26Mar2009(thur)27Mar2009(fri)28Mar2009(sat)']
        splitted_text = text_analyzer.split_text('Rewards 26Mar2009(thur) 27Mar2009(fri) 28Mar2009(sat)')
        self.assertListEqual(expected_splitted_text, splitted_text)

    def test_split_text_without_comma(self):
        """See if the text format passes for a text without colon and comma in only one string"""
        expected_splitted_text = ['Rewards', '26Mar2009(thur)27Mar2009(fri)28Mar2009(sat)']
        splitted_text = text_analyzer.split_text('Rewards: 26Mar2009(thur) 27Mar2009(fri) 28Mar2009(sat)')
        self.assertListEqual(expected_splitted_text, splitted_text)

    def test_split_text_without_colon(self):
        """See if the text format passes for a text without colon and comma in only one string"""
        expected_splitted_text = ['Rewards26Mar2009(thur)', '27Mar2009(fri)', '28Mar2009(sat)']
        splitted_text = text_analyzer.split_text('Rewards26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)')
        self.assertListEqual(expected_splitted_text, splitted_text)


if __name__ == '__main__':
    unittest.main()
