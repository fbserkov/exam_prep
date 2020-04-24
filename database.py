from datetime import date


class Database:
    def __init__(self):
        self._right_answers = tuple(
            line.strip().replace(' ', '') for line in open('right_answers'))
        self._my_answers = []
        for line in open('my_answers'):
            _date, _ticket, _question, _answer = line.split()
            _date = None if _date == 'None' else date(
                *map(int, _date.split('-')))
            self._my_answers.append(
                (_date, int(_ticket), int(_question), int(_answer)))

    def get_result(self, table_name, ticket, question):
        if table_name == 'right_answers':
            return int(self._right_answers[ticket - 1][question - 1])
        if table_name == 'my_answers':
            return tuple(_ for _ in self._my_answers if (
                ticket, question) == (_[1], _[2]))


if __name__ == '__main__':
    pass  # for tests
