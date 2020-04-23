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


class Data:
    def __init__(self):
        self._db = Database()

    def get_right_answer(self, ticket, question):
        return self._db.get_result('right_answers', ticket, question)

    def get_my_answers(self, ticket, question):
        return self._db.get_result('my_answers', ticket, question)

    def get_fallacy(self, ticket, question):
        right_answer = self.get_right_answer(ticket, question)
        my_answers = tuple(_[3] for _ in self.get_my_answers(ticket, question))
        return 1 - my_answers.count(right_answer) / len(my_answers)


def print_fallacy_rating():
    result = tuple(
        (i + 1, j + 1, data.get_fallacy(ticket=i+1, question=j+1))
        for i in range(40) for j in range(20)
    )
    result = sorted(result, key=lambda _: _[2])
    for ticket, question, fallacy in result:
        print(f'{fallacy:.2f}: Билет № {ticket}, Вопрос № {question}')


if __name__ == '__main__':
    data = Data()
    print_fallacy_rating()
