import unittest
from drinksin import get_contents

#polymorphism

class Tester(unittest.TestCase):
    def TestCase1(self):
        #instantiation of softdrink class
        new_softdrink = softdrinks()
        new_softdrink.set_type(20)
        self.assertEqual(get_contents(new_softdrink),[])

    def TestCase2(self):
        #instantiation of softdrink class
        new_softdrink2 = softdrinks()
        new_softdrink2.set_type(20)
        self.assertEqual(get_contents(new_softdrink),[])
