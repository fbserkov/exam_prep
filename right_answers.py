import os


class RightAnswers:
    def __init__(self, filename):
        self._right_answers = tuple(
            line.strip().replace(' ', '') for line in open(filename)
            if not line.startswith('#')
        )

    def get_value(self, ticket, question):
        return int(self._right_answers[ticket - 1][question - 1])


if __name__ == '__main__':
    filename = 'right_answers_test'
    with open(filename, 'w') as file:
        file.write('# Комментарий\n123\n246\n369\n')
    right_answers = RightAnswers(filename)
    assert right_answers.get_value(ticket=1, question=1) == 1
    assert right_answers.get_value(ticket=2, question=2) == 4
    assert right_answers.get_value(ticket=3, question=3) == 9
    os.remove(filename)
