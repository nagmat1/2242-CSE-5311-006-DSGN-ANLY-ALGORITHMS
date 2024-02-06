# Nagmat Nazarov 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Split array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Merge the two halves into a sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from left and right halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Test the merge sort implementation
arr = [5, 2, 4, 7, 1, 3, 2, 6]
sorted_arr = merge_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)
