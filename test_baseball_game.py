from unittest import TestCase

from baseball_game import Baseball, GameResult


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Baseball()
        self.game.answer = "123"

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

    def test_return_solve_result_if_matched_number(self):
        self.assert_matched_number(self.game.guess("123"), True, 3, 0)

    def test_return_unmatched_number(self):
        self.assert_matched_number(self.game.guess("456"), False, 0, 0)

    def assert_matched_number(self, result, solved, strikes, balls):
        self.assertIsNotNone(result)
        self.assertEqual(solved, result.solved)
        self.assertEqual(strikes, result.strikes)
        self.assertEqual(balls, result.balls)

