import Card
import os
import time
import Mode_interface
import MenuTEST



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
            rate_list = elem.get_word_rates()
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
            Mod = Mode_interface.ModeWrite(self)
            print("Режим 'Письмо'", '\n')
        elif mode == 2:
            Mod = Mode_interface.ModeChoice(self)
            print("Режим 'Тест'", '\n')

        i = 0
        Mod.create_sequence(mode)
        while ((i <= len(Mod.get_cards())) and (i < len(Mod.get_cards()) * 2)):
            print("Введите 'q' чтобы выйти из режима", '\n')
            current_card = Mod.get_sequence()[i][0]
            if mode == 1:
                print("Как переводится это слово:", current_card.get_card_content()[0], '\n')
                user_input = input("Введите перевод")
            elif mode == 2:
                print("Слово:", current_card.get_card_content()[0], '\n')
                true_index, current_set = Mod.random_words(i, Mod.get_sequence())
                print("Выберите номер варианта", '\n', *[x[0].get_card_content()[1] for x in current_set[:4]])
                user_input = input()
            if (user_input == 'q'):
                break

            if mode == 1:
                answer = Mod.check(user_input, i, Mod.get_sequence())
            elif mode == 2:
                answer = Mod.check(int(user_input), true_index, Mod.get_sequence())
            if answer:
                print("Правильно!")
            else:
                print("Неправильно")
            Mod.change_rate(mode, Mod.get_sequence()[i][1], answer)
            i += 1
            time.sleep(2)
            if os.name == 'posix':  # Для Unix-подобных систем (Linux, macOS)
                os.system('clear')
            elif os.name == 'nt':  # Для Windows
                os.system('cls')
