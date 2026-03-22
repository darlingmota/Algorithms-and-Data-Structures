
# Sorting Algorithms Benchmark – Vehicles Dataset

This project is part of my Algorithms and Data Structures assignment.

I implemented and compared different sorting algorithms in Python using a real world dataset of vehicles.

## What I did

- Loaded a dataset of ~100,000 vehicle records from a CSV file
- Built a data model using classes (`Vehicle`, `VehicleCollection`)
- Implemented 5 sorting algorithms from scratch:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort
  - Merge Sort
- Measured execution time using `time.perf_counter()`
- Compared performance as dataset size increased
- Analysed results vs theoretical time complexity

## Project Structure

- `main.py` – runs the program
- `model.py` – handles data and objects
- `sort.py` – contains all sorting algorithms
- `benchmark.py` – runs timing experiments
- `vehicles.csv` – dataset used

## Key Results

- Bubble, Selection, and Insertion Sort become very slow as data increases (O(n²))
- Quick Sort and Merge Sort scale much better (O(n log n))
- Quick Sort was the fastest in most cases

## How to run

Make sure all files are in the same folder, then run:

```bash
python main.py
