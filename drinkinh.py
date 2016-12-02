from drinks import Drinks

#inheritance
class beverages(Drinks):
    __type = 'coffee'

    def _init_(self):
        super(Drinks, self)._init_()
        self.__type = "coffee"

    def set_type(self, types):
        self.__type = types

    def get_type(self):
        return self.__type

class softdrinks(Drinks):
    __type = 'coke'

    def _init_(self):
        super(Clothes, self)._init_()
        self.__type = "coke"

    def set_type(self, types):
        self.__type = types

    def get_type(self):
        return self.__type