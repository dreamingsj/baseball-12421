class Baseball:
    def guess(self, number: str):
        if number is None:
            raise TypeError()

        if len(number) != 3:
            raise TypeError()