from model import VehicleCollection
from benchmark import run_price_benchmark, run_year_benchmark


def main():
    #create collection and load data 
    collection = VehicleCollection()
    collection.load_from_csv("vehicles.csv")
    #run first experiment 
    print("Price Benchmark")
    price_results = run_price_benchmark(collection)
    #run seconde experiment
    print("Year Benchmark")
    year_results = run_year_benchmark(collection)

    print("Done.")

#run program
if __name__ == "__main__":
    main()