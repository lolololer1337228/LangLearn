import Kit.py
import Card.py


class ModeStrategy(object):
    def __init__(self, flag, sequence):
        self.__flag = flag
        self.sequence = sequence

    def create_sequence(self, kit: Kit) -> list(Card):
        raise NotImplementedError

    def change_rate(self, boolean):
        raise NotImplementedError

    def change_word_translation(self, boolean):
        raise NotImplementedError

    def next_word(self, boolean) -> None:
        raise NotImplementedError


class ModeWrite(ModeStrategy):
    def check(answer, index):
        return answer == self.sequence[index].get_card_content()[1]


class ModeRotate
