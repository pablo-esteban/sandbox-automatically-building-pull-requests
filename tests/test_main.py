import unittest

from stormyweather.main import amazing_foo


class TestMain(unittest.TestCase):

    def test_should_run_without_raising_error(self):
        try:
            amazing_foo()
        except ValueError:
            self.fail()
