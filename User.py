class User:
    def __init__(self, __kits, __email, __username, __level):
        self.__kits = [kits() for i in range(kits) ];
        self.__email;
        self.__username;
        self.__level;
        print ("The User was built")

    def add_kit(self, __kits):
        self.__kits.append(input());
