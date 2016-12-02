#class that is called drink
class Drinks():
    colour=''
    price=0
    ingredient=''
    quantit=''
    def init(self, colours,prices,ingredients,quantity):
        self.colour=colours
        self.price=prices
        self.ingredient=ingredients
        self.quantit=quantity
        def set_colour(self, colours):
            self.colour=colours
        def set_price(self, prices):
            self.price=prices
        def set_ingredient(self, ingredients):
            self.ingredient=ingredients
        def set_quantit(self, quantity):
            self.quantit=quantity
        def get_colour(self):
            return colour
        def get_price(self):
            return price
        def get_ingredient(self):
            return ingredient
        def get_quantit(self):
            return quantity