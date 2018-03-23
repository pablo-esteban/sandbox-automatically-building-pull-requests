import unittest

from stormyweather.main import the_most_powerful_foo


class TestMain(unittest.TestCase):

    def test_should_run_without_raising_error(self):
        try:
            the_most_powerful_foo()
        except Exception as e:
            self.fail(str(e))
