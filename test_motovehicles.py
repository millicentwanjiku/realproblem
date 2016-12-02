from motorvehicles import MotorVehicles, Bicycle, SaloonCar
from unittest import TestCase


class TestMotors(TestCase):

    def test_number_of_bicycle_tyres(self):
        bike = Bicycle(2)
        self.assertEqual(bike.bicycle_tyres(), 2)

    def test_bicycle_name(self):
        bike = Bicycle(2)
        self.assertEqual(bike.motor_name(), "Bicycle")

    def test_number_of_saloon_tyres(self):
        saloon = SaloonCar(4)
        self.assertEqual(saloon.saloon_tyres(), 4)

    def test_saloon_name(self):
        saloon = SaloonCar(4)
        self.assertEqual(saloon.motor_name(), "Saloon Car")
