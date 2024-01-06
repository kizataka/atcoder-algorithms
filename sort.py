# Bubbleソート(O(n^2))
def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


# Selectionソート(O(n^2))
def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


# Insertionソート(O(n^2))
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


# Quickソート(O(nlogn))
def partition(numbers, low, high):
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i+1

def quikck_sort_1(numbers):
    def _quick_sort(numbers, low, high):
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick_sort(numbers, low, partition_index-1)
            _quick_sort(numbers, partition_index+1, high)
    _quick_sort(numbers, 0, len(numbers)-1)
    return numbers

def quick_sort_2(numbers):
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers.pop(0)
    left = [i for i in numbers if i <= pivot]
    right = [i for i in numbers if i > pivot]

    left = quick_sort_2(left)
    right = quick_sort_2(left)

    return left + [pivot] + right


# Mergeソート(O(nlogn))
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    # リストを二つに分割
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    # 並び替え処理
    i = j = k = 0
    # 左右のリストを調べ、小さい方の要素から順に結合リストに追加
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    # 左リストに残った要素を結合リストに追加
    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    # 右リストに残った要素を結合リストに追加
    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers