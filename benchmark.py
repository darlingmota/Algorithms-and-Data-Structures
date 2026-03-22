import time

from sort import bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort


def measure_time(sort_func, data, key):
    arr = data[:]

    start = time.perf_counter()
    sort_func(arr, key)
    end = time.perf_counter()

    return end - start


def average_time(sort_func, data, key, runs=1):
    times = []
    for _ in range(runs):
        t = measure_time(sort_func, data, key)
        times.append(t)
    return sum(times) / len(times)


def run_price_benchmark(collection):
    sizes = [250]

    algorithms = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick": quick_sort,
        "Merge": merge_sort
    }

    results = []

    for size in sizes:
        subset = collection.get_subset(size)[:50]  # temporarily limit to 50 for debugging
        row = {"Size": size}

        print(f"\nTesting size: {size}")

        for name, func in algorithms.items():
            print(f"Running {name}...")
            import sys; sys.stdout.flush()
            avg = average_time(func, subset, "price")
            row[name] = avg
            print(f"{name}: {avg:.5f}s")

        results.append(row)

    return results


def run_year_benchmark(collection):
    years = [2020, 2021, 2022, 2023, 2024]

    algorithms = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick": quick_sort,
        "Merge": merge_sort
    }

    results = []

    for year in years:
        data = collection.filter_by_year(year)[:50]  # temporarily limit to 50 for debugging
        row = {"Year": year}

        print(f"\nTesting year: {year}")

        for name, func in algorithms.items():
            print(f"Running {name}...")
            import sys; sys.stdout.flush()
            avg = average_time(func, data, "mileage")
            row[name] = avg
            print(f"{name}: {avg:.5f}s")

        results.append(row)

    return results