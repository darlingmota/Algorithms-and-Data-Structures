import csv

class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, mileage, engine_size, price):
        self.vehicle_id = int(vehicle_id)
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.engine_size = float(engine_size)
        self.price = float(price)
