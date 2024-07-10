from unittest import TestCase

from baseball_game import Baseball, GameResult


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

    def test_return_solve_result_if_matched_number(self):
        self.game.answer = "123"
        result: GameResult = self.game.guess("123")

        self.assertIsNotNone(result)
        self.assertTrue(result.solved)
        self.assertEqual(3, result.strikes)
        self.assertEqual(0, result.balls)

    def test_return_unmatched_number(self):
        self.game.answer = "123"
        result = self.game.guess("456")

        self.assertIsNotNone(result)
        self.assertFalse(result.solved)
        self.assertEqual(0, result.strikes)
        self.assertEqual(0, result.balls)

