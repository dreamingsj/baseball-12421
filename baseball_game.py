class GameResult:
    def __init__(self, solved, strikes, balls):
        self.solved = solved
        self.strikes = strikes
        self.balls = balls


class Baseball:
    def __init__(self):
        self.answer = ""
        self.strike = 0
        self.ball = 0

    def guess(self, number: str) -> GameResult:
        self.assert_illegal_value(number)
        if number == self.answer:
            return GameResult(True, 3, 0)
        else:
            n1, n2, n3 = number
            a1, a2, a3 = self.answer
            self.cal_strike_and_ball(a1, n1)
            self.cal_strike_and_ball(a2, n2)
            self.cal_strike_and_ball(a3, n3)
            return GameResult(False, self.strike, self.ball)

    def cal_strike_and_ball(self, a, n):
        if n in self.answer:
            if n == a:
                self.strike += 1
            else:
                self.ball += 1

    def assert_illegal_value(self, number):
        if number is None:
            raise TypeError()
        if len(number) != 3:
            raise TypeError()
        for n in number:
            if not ord('0') <= ord(n) <= ord('9'):
                raise TypeError()
        n1, n2, n3 = number
        if n1 == n2 or n2 == n3 or n1 == n3:
            raise TypeError()
