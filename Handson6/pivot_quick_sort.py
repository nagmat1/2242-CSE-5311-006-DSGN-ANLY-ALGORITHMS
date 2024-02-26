import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    """
    This function takes the last element as pivot, places
    the pivot element at its correct position in the sorted
    array, and places all smaller (smaller than pivot)
    to the left of the pivot and all greater elements to
    the right of the pivot.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    """
    The main function that implements QuickSort
    arr: List to be sorted
    low: Starting index
    high: Ending index
    """
    if low < high:
        # Partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)
        # Separately sort elements before partition and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def generate_random_array(size):
    """
    Generates a random array of given size.
    """
    return [random.randint(1, 1000) for _ in range(size)]

def generate_sorted_array(size):
    """
    Generates a sorted array of given size.
    """
    return [i for i in range(1, size + 1)]

def generate_reversed_array(size):
    """
    Generates a reversed sorted array of given size.
    """
    return [i for i in range(size, 0, -1)]

# Benchmarking sizes
sizes = [100, 500, 1000, 5000, 10000]

import sys
sys.setrecursionlimit(150000)

# Benchmarking best case
best_case_times = []
for size in sizes:
    data = generate_sorted_array(size)
    start_time = time.time()
    quicksort(data,0,len(data)-1)
    end_time = time.time()
    best_case_times.append(end_time-start_time)

# Benchmarking worst case
worst_case_times = []
for size in sizes:
    data = generate_reversed_array(size)
    start_time = time.time()
    quicksort(data, 0, len(data) - 1)
    end_time = time.time()
    worst_case_times.append(end_time-start_time)

# Benchmarking average case
average_case_times = []
for size in sizes:
    data = generate_random_array(size)
    start_time = time.time()
    quicksort(data, 0, len(data) - 1)
    end_time = time.time()
    average_case_times.append(end_time-start_time)

print("Average time take = {} ".format(average_case_times))

# Plotting the results
plt.plot(sizes, best_case_times, label='Best Case')
plt.plot(sizes, worst_case_times, label='Worst Case')
plt.plot(sizes, average_case_times, label='Average Case')
plt.xlabel('Array Size')
plt.ylabel('Time Taken (seconds)')
plt.title('Quicksort Performance')
plt.legend()
plt.grid(True)
plt.savefig("result.png")
plt.show()
