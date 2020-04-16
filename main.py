def read_my_answers():
    my_answers = [line.strip().replace(' ', '') for line in open('my_answers')]
    # dates: from datetime import date
    print(my_answers)


class Data:
    def __init__(self):
        self._right_answers = [
            line.strip().replace(' ', '') for line in open('right_answers')]

    def get_right_answer(self, ticket, question):
        return self._right_answers[ticket - 1][question - 1]


if __name__ == '__main__':
    data = Data()
    print(data.get_right_answer(ticket=10, question=15))
    read_my_answers()
