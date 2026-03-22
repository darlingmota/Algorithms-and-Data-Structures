import csv

# this class represents one vehicle which is one row form the CSV
class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, mileage, engine_size, price):
        self.vehicle_id = vehicle_id # kept as string
        self.brand = brand 
        self.model = model
        self.year = int(year)
        self.mileage = int(mileage)
        self.engine_size = float(engine_size)
        self.price = float(price)

#this class stores and manages all behicles 
class VehicleCollection:
    def __init__(self):
        self.vehicles = [] # list to store all vehicle objects 
    # loads vehicles from CSV file
    def load_from_csv(self, filename):
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)# skip header row
            for row in reader:
                v = Vehicle(*row) # create vehicle object from row
                self.vehicles.append(v)
    # returns all vehicles 
    def get_all(self):
        return self.vehicles
    # returns first n vehicles 
    def get_subset(self, n):
        return self.vehicles[:n]
    # filters vehicles by year 
    def filter_by_year(self, year):
        return [v for v in self.vehicles if v.year == year]