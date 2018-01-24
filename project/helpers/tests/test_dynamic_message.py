import unittest
import sys

from .. import dynamic_message


class DynamicMessageTest(unittest.TestCase):
    """Tests for the ``dynamic_message()`` function."""

    # def test_function_runs(self):
    #     """Basic smoke test: does the function run."""
    #     with self.assertRaises(SystemExit) as cm:
    #         dynamic_message.show_error_message_and_quit('message')
    #     self.assertEqual(cm.exception.code, 1)
    #
    def test_sys_exit_exception(self):
        with self.assertRaises(SystemExit) as e:
            sys.exit('exit_with_err')
        self.assertTrue(isinstance(e.exception, SystemExit))
        self.assertEqual(e.exception.code, 'exit_with_err')
        self.assertEqual(e.exception.message, 'exit_with_err')
        self.assertEqual(e.exception.args, ('exit_with_err',))

    # def test_show_error_msg_exception(self):
    #     # Test the exception type
    #     with self.assertRaises(SystemExit) as e:
    #         dynamic_message.show_error_message_and_quit('message')
    #     self.assertTrue(isinstance(e.exception, SystemExit))
    #
    # def test_show_error_msg(self):
    #     # Test the exception type
    #     with self.assertRaises(SystemExit) as e:
    #         dynamic_message.show_error_message_and_quit('exit_with_err')
    #     self.assertEqual(e.exception.message, 'exit_with_err')


if __name__ == '__main__':
    unittest.main()
