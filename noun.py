class Noun:

    def __init__(self, nominative, **cases):
        self._dict = {'nominative': nominative}
        for case, value in cases.items():
            self._dict[case] = value

    def __getattr__(self, item):
        try:
            # TODO retrieve gettext translation
            return self._dict[item]
        except KeyError:
            # TODO invoke context gettext with fallback to nominative translation
            return self.nominative


if __name__ == '__main__':
    print(Noun('kaczka', accusative='kaczkę').accusative)  # kaczkę
    print(Noun('pies').accusative)  # pies (fallback)
    print(Noun('ble').fakecase)  # ble (fallback)
    print(Noun('ble', yetanotherfakecase='bum').yetanotherfakecase)  # bum
