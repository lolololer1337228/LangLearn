class ModeStrategy:
    def __init__(flag, card_kit):
        self.__flag = flag
        self.__card_kit = card_kit

    def create_sequence(self):
        return sorted(self.__card_kit, key=lambda x: -x.rate)

    def 
