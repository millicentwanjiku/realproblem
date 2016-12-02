from drinks import Drinks
from drinkinh import softdrinks

#instance method
def get_contents(objects):
    contents = [] #instance variable
    contents.append(objects.ingredient)
    contents.append(objects.quantit)
    contents.append(objects.colour)
    contents.append(objects.get_type())
    return contents