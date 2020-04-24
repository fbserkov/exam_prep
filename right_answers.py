class RightAnswers:
    def __init__(self, filename):
        self._right_answers = tuple(
            line.strip().replace(' ', '') for line in open(filename))

    def get_value(self, ticket, question):
        return int(self._right_answers[ticket - 1][question - 1])


if __name__ == '__main__':
    pass  # for tests
