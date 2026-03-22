def get_key(vehicle, key):
    return getattr(vehicle, key)

def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if get_key(arr[j], key) > get_key(arr[j + 1], key):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr, key):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if get_key(arr[j], key) < get_key(arr[min_index], key):
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

