import array
import Card

class Kit():
    def __init__(self, name, cards, progress):
      self.__name = name
      self.__card_array = cards
      self.__progress = progress

    def get_name_kit(self) -> str:
        return self.__name

    def get_array_of_kit(self) -> array:
        return self.__card_array

    def change_name(self, new_name) -> bool:
        old_name = self.__name
        self.__name = new_name
        return self.__name != old_name

    def add_card(self, new_card) -> None:
        self.__card_array.append(new_card)

    def remove_card(self, card_index) -> None:
        self.__card_array.pop(card_index)

    def progress_counter(self) -> float:
        sum_rate = 0
        for elem in self.__card_array:
            sum_rate += elem.get_rate_1() + elem.get_rate_2() + elem.get_rate_3()
        return sum_rate / len(self.__card_array)



