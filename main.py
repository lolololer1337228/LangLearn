import array
import Card

class Kit():
    def __init__(self, name, cards, progress):
      self.__name = name
      self.__card_array = cards
      self.__progress = progress

    def __change_name(self, new_name):
        old_name = self.__name
        self.__name = new_name
        return self.__name != old_name

    def __add_card__(self, new_card):
        self.__card_array.append(new_card)

    def __remove_card(self, card):
        
