Import Kit
Import Card

class User:
    def __init__(self, __kits:list(Kit), __email:str, __username:str, __level):
        self.__kits = [kits() for i in range(kits) ];
        self.__email;
        self.__username;
        self.__level;
        print ("The User was built")

    def add_kit(self, kit:Kit) -> None:
        name = input()
        k = kit(name)
        self.__kits.append(k)

    def show_kits(self) -> None:
        for i in range(len(self.__kits)):
            print(i, self.__kits[i].get_name_kit)

    def show_element_of_kit(self, i:int) -> None:
        Ar = self.__kits[i]
        CardList = Ar.get_array_of_kit()
        for j in range(len(Ar)):
            print(j, CardList[j].get_card_content[0], CardList[j].get_card_content[1])

    def show_progress(self, i:int) -> None:
        Ar = self.__kits[i]
        print(Ar.get_progress())