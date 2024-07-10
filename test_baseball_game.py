from unittest import TestCase

from baseball_game import Baseball


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Baseball()

    def test_exception_input_is_none(self):
        with self.assertRaises(TypeError):
            self.game.guess(None)
