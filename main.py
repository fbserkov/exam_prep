from datetime import date


def read_my_answers():
    my_answers = tuple(tuple([] for _ in range(20)) for _ in range(40))
    for line in open('my_answers'):
        _date, _ticket, _question, _answer = line.split()
        if _date == 'None':
            _date = None
        else:
            _date = date(*map(int, _date.split('-')))
        my_answers[int(_ticket) - 1][int(_question) - 1].append(
            (_date, int(_answer)))
    return my_answers


class Data:
    def __init__(self):
        self._right_answers = tuple(
            line.strip().replace(' ', '') for line in open('right_answers'))
        self._my_answers = read_my_answers()

    def get_right_answer(self, ticket, question):
        return self._right_answers[ticket - 1][question - 1]

    def get_my_answer(self, ticket, question):
        return self._my_answers[ticket - 1][question - 1]


if __name__ == '__main__':
    data = Data()
    print(data.get_my_answer(13, 16))
