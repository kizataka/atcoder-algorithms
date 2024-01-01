# Bubbleソート
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


# Selectionソート
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


# Insertionソート
def insertion_sort(numbers):
    n = len(numbers)
    for i in range(1, n):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


# Quickソート
def partition(numbers, low, high):
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

def quikck_sort(numbers):
    def _quick_sort(numbers, low, high):
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers


# Mergeソート
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers