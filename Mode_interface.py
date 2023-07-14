import Kit
import Card
import random


class ModeStrategy(object):
    def __init__(self, kit: Kit, mode):
        self.__flag = True
        self.__kit = kit
        self.__sequence = []
        self.__mode = mode

    def __rate_filter(self, card_list: list, mode, limit):  # фильтр для взятия слов с определённым рейтингом
        filter_list = []
        for elem in card_list:
            if(elem[0].get_word_rates[mode]) <= limit:
                filter_list.append(elem)
        return filter_list

    def create_sequence(self, __kit: Kit, mode) -> list(Card):
        card_list = __kit.get_card_list()
        number_sequence = []
        for i in range(0, len(card_list)):
            number_sequence[i] = i
        card_list = list(zip(card_list, number_sequence))  # присваиваем каждой карточке её индекс в наборе (kit)
        self.__sequence = random.shuffle(card_list)
        sequence08 = random.shuffle(self.__rate_filter(card_list, mode, 0.8))
        self.__sequence += sequence08
        if len(self.__sequence) <= 2 * len(card_list):  # следим, чтобы последовательность не была слишком большой
            sequence05 = random.shuffle(self.__rate_filter(card_list, mode, 0.5))
            self.__sequence += sequence05
            if len(self.__sequence) <= 2 * len(card_list):
                sequence03 = random.shuffle(self.__rate_filter(card_list, mode, 0.3))
                self.__sequence += sequence03
        del self.__sequence[2 * len(card_list):]

        # обрезаем последовательность до размера 2n

    def change_rate(self, kit: Kit, mode, index, is_correct):
        if is_correct:
            kit.get_card_list()[index].get_word_rates()[mode] += 0.4  # увеличиваем рейтинг слова
            if kit.get_card_list()[index].get_word_rates()[mode] > 1:
                kit.get_card_list()[index].get_word_rates()[mode] = 1
        else:
            kit.get_card_list()[index].get_word_rates()[mode] -= 0.4
            if kit.get_card_list()[index].get_word_rates()[mode] < 0:
                kit.get_card_list()[index].get_word_rates()[mode] = 0

    def change_word_translation(self, boolean):
        for i in range (0, len(self.__sequence)):
            self.__sequence[i][0].get_card_content()[0], self.__sequence[i][0].get_card_content()[1]\
                = self.__sequence[i][0].get_card_content()[1], self.__sequence[i][0].get_card_content()[0]

    def get_card(self, index):
       return self.__sequence[index]

    def get_len(self):
        return len(self.__sequence)


class ModeChoice(ModeStrategy):
    def random_words(self, answer, index):
        alternative = [answer, 0, 0, 0]
        for i in range (1,3):
            alternative[i] = random.choise(self.__sequence)


   # def label(self, is_correct) -> bool:
   #     pass


class ModeWrite(ModeStrategy):
    def check(self, answer, index):
        return answer == self.sequence[index].get_card_content()[1]


