import heapq

def merge_sorted_arrays(arrays):
    merged_result = []
    heap = []

    # Initialize the heap with the first element from each array
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))  # (value, array index, index within array)

    while heap:
        val, arr_idx, idx_within_arr = heapq.heappop(heap)
        merged_result.append(val)

        # Move to the next element in the array
        idx_within_arr += 1
        if idx_within_arr < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][idx_within_arr], arr_idx, idx_within_arr))

    return merged_result

# Example usage
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]

merged_array = merge_sorted_arrays([array1, array2, array3])
print(merged_array)
