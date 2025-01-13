def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_hybrid(arr, low, high):
    while low < high:
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            p = partition(arr, low, high)
            if p - low < high - p:
                quick_sort_hybrid(arr, low, p - 1)
                low = p + 1
            else:
                quick_sort_hybrid(arr, p + 1, high)
                high = p - 1
