from unittest import TestCase

from baseball_game import Baseball


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Baseball()

    def assert_input_is_wrong(self, number):
       try:
            self.game.guess(number)
            self.fail()
       except TypeError:
            pass

    def test_exception_when_input_is_wrong(self):
        self.assert_input_is_wrong(None)
        self.assert_input_is_wrong("12")
        self.assert_input_is_wrong("1234")
        self.assert_input_is_wrong("12s")
        self.assert_input_is_wrong("121")


