class User:
    def __init__(self, __kits:kit, __email:str, __username:str, __level):
        self.__kits = [kits() for i in range(kits) ];
        self.__email;
        self.__username;
        self.__level;
        print ("The User was built")

    def add_kit(self, __kit) -> None:
        self.__kits.append(__kit)

    def