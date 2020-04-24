from database import Database
from right_answers import RightAnswers


class MyAnswers:
    def __init__(self):
        self._right_answers = RightAnswers(filename='right_answers')
        self._my_answers = Database(filename='my_answers')

    def get_my_answers(self, ticket, question):
        return self._my_answers.get_value(ticket, question)

    def get_fallacy(self, ticket, question):
        right_answer = self._right_answers.get_value(ticket, question)
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
    data = MyAnswers()
    print_fallacy_rating()
