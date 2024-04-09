#include <iostream>

class DynamicArray {
private:
    int* arr;
    int capacity;
    int size;

public:
    DynamicArray() : arr(nullptr), capacity(0), size(0) {}

    ~DynamicArray() {
        delete[] arr;
    }

    // Function to add an element to the dynamic array
    void push_back(int value) {
        // If the array is full, resize it
        if (size == capacity) {
            // If capacity is 0, set it to 1, else double the capacity
            capacity = (capacity == 0) ? 1 : capacity * 2;
            int* newArr = new int[capacity];
            // Copy existing elements to the new array
            for (int i = 0; i < size; ++i) {
                newArr[i] = arr[i];
            }
            // Delete old array and point to the new array
            delete[] arr;
            arr = newArr;
        }
        // Add the new element at the end and increment size
        arr[size++] = value;
    }

    // Function to get an element at a specific index
    int at(int index) const {
        if (index < 0 || index >= size) {
            std::cerr << "Index out of bounds\n";
            return -1; // Returning a default value, you may handle this differently based on your requirements
        }
        return arr[index];
    }

    // Function to get the current size of the dynamic array
    int getSize() const {
        return size;
    }
};

int main() {
    DynamicArray arr;

    // Add elements to the dynamic array
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);

    // Access elements using the at() function
    std::cout << "Element at index 0: " << arr.at(0) << std::endl;
    std::cout << "Element at index 1: " << arr.at(1) << std::endl;
    std::cout << "Element at index 2: " << arr.at(2) << std::endl;

    return 0;
}
