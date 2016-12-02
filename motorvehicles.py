class MotorVehicles:

    def __init__(self):
        self.name = ""


class Bicycle(MotorVehicles):

    def __init__(self, tyres):
        self.tyres = tyres

    def motor_name(self):
        self.name = "Bicycle"
        return self.name

    def bicycle_tyres(self):
        return self.tyres


class SaloonCar(MotorVehicles):

    def __init__(self, tyres):
        self.tyres = tyres

    def motor_name(self):
        self.motor_name = "Saloon Car"
        return self.motor_name

    def saloon_tyres(self):
        return self.tyres
