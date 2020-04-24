from datetime import date


class Database:
    def __init__(self, filename):
        self._data = []
        for line in open(filename):
            _date, _ticket, _question, _answer = line.split()
            _date = None if _date == 'None' else date(
                *map(int, _date.split('-')))
            self._data.append(
                (_date, int(_ticket), int(_question), int(_answer)))

    def get_value(self, ticket, question):
        return tuple(_ for _ in self._data if (
            ticket, question) == (_[1], _[2]))


if __name__ == '__main__':
    pass  # for tests
