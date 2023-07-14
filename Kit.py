import Card
import os
import time
import Mode_interface



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

    def StartModule(self, mode):
        if mode == 1:
            Mod = Mode_interface.ModeWrite(self, mode)
            print("Режим 'Письмо'", '/n')
        elif mode == 2:
            Mod = Mode_interface.ModeChoice(self, mode)
            print("Режим 'Тест'", '/n')

        Mod.create_sequence(self, mode)
        i = 0
        while (i != Mod.get_len()):
            print("Введите 'q' чтобы выйти из режима", '\n')
            current_card = Mod.get_card(i)
            print("Как переводится это слово:", current_card.get_card_content()[0], '\n')
            user_input = input("Введите перевод")
            if (user_input == 'q') or ():
                break

            if mode == 1:
                answer = Mod.check(user_input, i)
            #elif mode == 2:
            #    answer =
            if answer:
                print("Правильно!")
            else:
                print("Неправильно")
            Mod.change_rate(self, mode, i, answer)
            i += 1
            time.sleep(2)
            os.system('cls')





