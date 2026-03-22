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

def insertion_sort(arr, key):
    n = len(arr)
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and get_key(arr[j], key) > get_key(current, key):
            arr[j + 1] = arr[j]
            j -+ 1
            arr[j + 1] = current

def quick_sort(arr, key):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)
    
    def partition(items, low, high):
        pivot = get_key(items[high], key)
        i = low - 1
        for j in range(low, high):
            if get_key(items[j], key) <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                items[i + 1], items[high] = items[high], items[i + 1]
                return i + 1
            _quick_sort(arr, 0, len(arr) - 1)

def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, key)
        merge_sort(right, key)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if get_key(left[i], key) < get_key(right[j], key):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1 
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1