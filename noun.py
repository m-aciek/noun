class Noun:
    ALLOWED_CASES = ('accusative', 'dative', 'ablative', 'genitive', 'vocative', 'locative', 'instrumental')

    def __init__(self, nominative, **cases):
        self._dict = {'nominative': nominative}
        for case, value in cases.items():
            if case in self.ALLOWED_CASES:
                self._dict[case] = value
            else:
                raise TypeError(f"__init__() got an unexpected keyword argument '{case}'")

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            # TODO invoke context gettext with fallback to nominative translation
            if item in self.ALLOWED_CASES:
                return self.nominative
            raise AttributeError(f'{item} is not allowed noun grammatical case.')


if __name__ == '__main__':
    print(Noun('kaczka', accusative='kaczkę').accusative)
    print(Noun('pies').accusative)
    # print(Noun('ble').fakecase)  # raises AttributeError
    # print(Noun('ble', vocative='bum'))  # raises TypeError
