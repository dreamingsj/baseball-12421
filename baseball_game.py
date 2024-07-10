class Baseball:
    def guess(self, number: str):
        if number is None:
            raise TypeError()

        if len(number) != 3:
            raise TypeError()

        for n in number:
            if not ord('0') <= ord(n) <= ord('9'):
                raise TypeError()