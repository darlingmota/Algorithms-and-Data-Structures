#helper function to get attrivut dynamically 
def get_key(vehicle, key):
    return getattr(vehicle, key)

# bubble sort
def bubble_sort(arr, key):
    n = len(arr)
    for i in range(n):# loop through entire list
        for j in range(0, n - i - 1):# compare adjacent elements
            if get_key(arr[j], key) > get_key(arr[j + 1], key):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]# swap if out of order

# selection sort
def selection_sort(arr, key):
    n = len(arr)
    for i in range(n):
        min_index = i#assume current is smallest
        for j in range(i + 1, n):#finds smallest element in remaining list
            if get_key(arr[j], key) < get_key(arr[min_index], key):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]#swap into correct position

# insertion sort
def insertion_sort(arr, key):
    for i in range(1, len(arr)):#start from second element
        current = arr[i]
        j = i - 1
        #shift elements to the right until correct sport is found
        while j >= 0 and get_key(arr[j], key) > get_key(current, key):
            arr[j + 1] = arr[j]
            j -= 1
        # insert element in correct position
        arr[j + 1] = current

# quick sort
def quick_sort(arr, key):
    #recursive quick sort
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)
    #partition function
    def partition(items, low, high):
        pivot = get_key(items[high], key)#choose last element as pivot
        i = low - 1
        for j in range(low, high):
            if get_key(items[j], key) <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]#place pivot in correct position
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
# merge sort
def merge_sort(arr, key):
    if len(arr) > 1:# only split if more than 1 element
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        # recursively split
        merge_sort(left, key)
        merge_sort(right, key)

        i = j = k = 0
        # merge two halves
        while i < len(left) and j < len(right):
            if get_key(left[i], key) < get_key(right[j], key):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1 
            k += 1
        # add remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1