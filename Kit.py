import Card



class Kit():
    def __init__(self, name):
      self.__name = name
      self.__card_list = []
      self.__progress = 0.0

    def get_name_kit(self) -> str:
        return self.__name

    def get_card_list(self) -> list:
        return self.__card_list

    def change_name(self, new_name) -> bool:
        old_name = self.__name
        self.__name = new_name
        return self.__name != old_name

    def add_card(self, new_card) -> None:
        self.__card_list.append(new_card)

    def remove_card(self, card_index) -> None:
        self.__card_list.pop(card_index)

    def __progress_counter(self) -> None:
        sum_rate = 0
        for elem in self.__card_list:
            rate_list = elem.get_rates()
            for now_rate in rate_list:
                sum_rate += now_rate
            self.__progress = (sum_rate / len(self.__card_list))

    def get_progress(self) -> float:
        self.__progress_counter()
        return self.__progress

    def reset_counter(self) -> None:
        self.__progress = 0

    #def start_mode(self, number_of_mode):
     #   if number_of_mode == 0:





