def remove_duplicates(array):
    # If array is empty or has only one element, no duplicates to remove
    if len(array) <= 1:
        return array

    # Initialize an empty list to store unique elements
    unique_array = [array[0]]

    # Iterate through the array starting from the second element
    for i in range(1, len(array)):
        # If the current element is different from the previous one, add it to the unique_array
        if array[i] != array[i - 1]:
            unique_array.append(array[i])

    return unique_array

# Test the function
array1 = [2, 2, 2, 2, 2]
array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]

print("Input:", array1)
print("Output:", remove_duplicates(array1))  # Output: [2]

print("Input:", array2)
print("Output:", remove_duplicates(array2))  # Output: [1, 2, 3, 4, 5]
