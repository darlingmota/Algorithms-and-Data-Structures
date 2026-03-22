import csv

class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, mileage, engine_size, price):
        self.vehicle_id = vehicle_id
        self.brand = brand 
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.engine_size = float(engine_size)
        self.price = float(price)

class VehicleCollection:
    def __init__(self):
        self.vehicles = []

    def load_from_csv(self, filename):
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                v = Vehicle(*row)
                self.vehicles.append(v)

    def get_all(self):
        return self.vehicles

    def get_subset(self, n):
        return self.vehicles[:n]

    def filter_by_year(self, year):
        return [v for v in self.vehicles if v.year == year]