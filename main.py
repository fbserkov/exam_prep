from datetime import date, timedelta


def read_my_answers():
    raw_data = (line.strip().replace(' ', '') for line in open('my_answers'))
    sequence_of_questions = (
        tuple(range(3, 21)) + (18, 17, 19, 20) +
        2 * tuple(range(1, 21)) + (1, 2)
    )
    raw_dates = (
        [
            None, date(2020, 3, 11), date(2020, 3, 12), date(2020, 3, 17),
            date(2020, 3, 19),
        ] +
        [date(2020, 3, 22) + timedelta(_) for _ in range(13)] +
        [date(2020, 4, 5) + timedelta(_) for _ in range(5)] +
        [date(2020, 4, 11) + timedelta(_) for _ in range(6)]
    )
    questions_per_date = (
        (2, 1, 1, 3, 1, 3, 2, 2, 3, 2, 4) + 14 * (2, ) + (3, 3, 4, 2))
    dates = ()
    for couple in zip(questions_per_date, raw_dates):
        dates += couple[0] * (couple[1], )

    my_answers = tuple(tuple([] for _ in range(20)) for _ in range(40))
    for i, ticket in enumerate(raw_data):
        for j, question in enumerate(ticket):
            my_answers[i][sequence_of_questions[j] - 1].append(
                (dates[j], int(question)))
    return my_answers


def read_my_answers_2():
    my_answers = tuple(tuple([] for _ in range(20)) for _ in range(40))
    for line in open('my_answers_table'):
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
        self._my_answers_2 = read_my_answers_2()

    def get_right_answer(self, ticket, question):
        return self._right_answers[ticket - 1][question - 1]

    def get_my_answer(self, ticket, question):
        return self._my_answers[ticket - 1][question - 1]

    def get_my_answer_2(self, ticket, question):
        return self._my_answers_2[ticket - 1][question - 1]


if __name__ == '__main__':
    data = Data()
    print(data.get_my_answer(13, 16))
    print(data.get_my_answer_2(13, 16))
