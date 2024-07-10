class Baseball:
    def guess(self, number: str):
        self.assert_illegal_value(number)

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