class ModeInterface:
    def __init__(flag, card_kit):
        self.__flag = flag
        self.__card_kit = card_kit

    def create_sequence(self):
        return self.__card_kit


