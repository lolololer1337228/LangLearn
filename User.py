import Kit
import Card


class User:
    def __init__(self, user:str):
        self.__kits = []
        self.__username = user
        #self.__level
        print ("The User was built")

    def get_username(self) -> str:
        return self.__username

    def get_count_kits(self):
        return len(self.__kits)

    def get_kit_by_ID(self, id) -> Kit:
        return self.__kits[id]

    def add_kit(self, kit:Kit) -> None:
        self.__kits.append(kit)

    def remove_kit(self, id):
        self.__kits.pop(id)

    def show_kits(self) -> None:
        for i in range(len(self.__kits)):
            print(i, self.__kits[i].get_name_kit())

    def show_kit(self, i) -> None:
        print(i, self.__kits[i].get_name_kit())

    def show_element_of_kit(self, i:int) -> None:
        CardList = self.__kits[i].get_card_list()
        for j in range(len(CardList)):
            print(j, CardList[j].get_card_content()[0], CardList[j].get_card_content()[1])

    def show_progress(self, i:int) -> None:
        Ar = self.__kits[i]
        print(Ar.get_progress())
