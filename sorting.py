# CLASS : 2242-CSE-5311-006-DSGN-ANLY-ALGORITHMS
# Nagmat Nazarov 1002186972 Hands On Week 2.

def insertionSort(arr):
    n = len(arr)

    if n<= 1:
        return

    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j = j -1
        arr[j+1]=key
        print(arr)
    return arr

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i

        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind = j
        (arr[i],arr[min_ind]) = (arr[min_ind],arr[i])
        print(arr)
    return arr

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j],arr[j+1]=arr[j+1],arr[j]
            print(arr)
        if not swapped:
            return arr
    return arr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Insertion Sort test
    arr = [12, 11, 13, 5, 6]
    print("In the beginning, Insertion Sort ==> {}".format(arr))
    arr = insertionSort(arr)
    print("Sorted array = {} ".format(arr))

    #Selection Sort
    arr = [12, 11, 13, 5, 6]
    print("Selection Sort, In the beginning ==>{}".format(arr))
    arr = selectionSort(arr)
    print("Sorted array = {} ".format(arr))

    # Bubble sort
    arr = [12, 11, 13, 5, 6]
    print("Bubble Sort, In the beginning ==> {}".format(arr))
    arr = bubbleSort(arr)
    print("Sorted array = {} ".format(arr))
