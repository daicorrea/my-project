import unittest
import sys

from .. import dynamic_message


class DynamicMessageTest(unittest.TestCase):
    """Tests for the ``dynamic_message()`` function."""

    def test_function_runs(self):
        """Basic smoke test: does the function run."""
        with self.assertRaises(SystemExit) as e:
            dynamic_message.show_error_message_and_quit('test_message')
        self.assertTrue(isinstance(e.exception, SystemExit))

    def test_sys_exit_exception_message(self):
        """Test the error message that is passed"""
        with self.assertRaises(SystemExit) as e:
            sys.exit('test_message')
        self.assertEqual(e.exception.code, 'test_message')

    def test_show_error_msg_exception(self):
        """Test the exception type"""
        with self.assertRaises(SystemExit) as e:
            dynamic_message.show_error_message_and_quit('test_message')
        self.assertTrue(isinstance(e.exception, SystemExit))

if __name__ == '__main__':
    unittest.main()
