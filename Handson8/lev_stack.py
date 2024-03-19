def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    stack = []
    stack.append((low, high))

    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def ith_order_statistic(arr, i):
    n = len(arr)
    if i < 0 or i >= n:
        return None
    quicksort(arr, 0, n - 1)
    return arr[i]

# Example usage:
arr = [12, 3, 5, 7, 4, 19, 26]
i = 2  # Find the 2nd smallest element
result = ith_order_statistic(arr, i)
print(f"The {i+1}th smallest element is: {result}")
