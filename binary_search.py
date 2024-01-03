# 二分探索(計算量はO(logn))

# リストの中に特定の要素が含まれているかを判定する関数
def binary_search(numbers, value):
    numbers = sorted(numbers)  # 二分探索はリストがソートされている時に有効、計算量はO(n*logn)
    left, right = 0, len(numbers) - 1  # leftとrightを初期化
    while left <= right:
        mid = (left + right) // 2  # 中間地点を定義
        if numbers[mid] == value:
            return True
        elif numbers[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False