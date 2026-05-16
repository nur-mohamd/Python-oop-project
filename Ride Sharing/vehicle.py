from abc import ABC 

class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 60,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_plate, rate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate

    def show_vehicle_info(self):
        print(f"Vehicle Type : {self.vehicle_type}")
        print(f"License Plate : {self.license_plate}")
        print(f"Rate : {self.rate}")
        
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)
        
class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate):
        super().__init__(vehicle_type, license_plate, rate)