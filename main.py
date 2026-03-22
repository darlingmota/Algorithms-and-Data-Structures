from model import VehicleCollection
from benchmark import run_price_benchmark, run_year_benchmark


def main():
    collection = VehicleCollection()
    collection.load_from_csv("vehicles.csv")

    print("Price Benchmark")
    price_results = run_price_benchmark(collection)

    print("Year Benchmark")
    year_results = run_year_benchmark(collection)

    print("Done.")


if __name__ == "__main__":
    main()