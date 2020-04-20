from datetime import date, timedelta


def read_my_answers():
    my_answers = tuple(tuple([] for _ in range(20)) for _ in range(40))
    raw_data = (line.strip().replace(' ', '') for line in open('my_answers'))
    sequence_of_questions = (
        tuple(range(3, 21)) + (18, 17, 19, 20) +
        2 * tuple(range(1, 21)) + (1, 2)
    )
    dates = (
        [
            None, date(2020, 3, 11), date(2020, 3, 12), date(2020, 3, 17),
            date(2020, 3, 19),
        ] +
        [date(2020, 3, 22) + timedelta(i) for i in range(13)] +
        [date(2020, 4, 5) + timedelta(i) for i in range(5)] +
        [date(2020, 4, 11) + timedelta(i) for i in range(6)]
    )
    questions_per_date = (
        (2, 1, 1, 3, 1, 3, 2, 2, 3, 2, 4) + 14 * (2, ) + (3, 3, 4, 2))
    print(sum(questions_per_date))
    return my_answers


class Data:
    def __init__(self):
        self._right_answers = [
            line.strip().replace(' ', '') for line in open('right_answers')]
        self._my_answers = read_my_answers()

    def get_right_answer(self, ticket, question):
        return self._right_answers[ticket - 1][question - 1]

    def get_my_answer(self, ticket, question):
        return self._my_answers[ticket - 1][question - 1]


if __name__ == '__main__':
    data = Data()
    print(data.get_my_answer(ticket=10, question=15))
