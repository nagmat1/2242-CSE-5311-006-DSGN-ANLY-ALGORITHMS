class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def partition(head, tail):
    if head == tail or head is None or tail is None:
        return head

    pivot = tail
    prev = None
    current = head
    while current != pivot:
        if current.data <= pivot.data:
            if not prev:
                head = current.next
            else:
                prev.next = current.next
            temp = current.next
            current.next = None
            tail.next = current
            tail = current
            current = temp
        else:
            if not prev:
                head = current.next
            else:
                prev.next = current.next
            temp = current.next
            current.next = head
            head = current
            current = temp
    return head

def get_tail(head):
    while head.next:
        head = head.next
    return head

def quicksort(head, tail):
    if head == tail or head is None or tail is None:
        return head

    new_head = partition(head, tail)
    if new_head != head:
        temp = new_head
        while temp.next != head:
            temp = temp.next
        temp.next = None
        new_head = quicksort(new_head, temp)
        temp = get_tail(new_head)
        temp.next = head
    new_tail = get_tail(new_head)
    new_tail.next = quicksort(new_tail.next, tail)
    return new_head

def ith_order_statistic(head, i):
    if head is None:
        return None
    tail = get_tail(head)
    head = quicksort(head, tail)
    current = head
    for _ in range(i):
        if current.next:
            current = current.next
        else:
            return None
    return current.data

# Example usage:
linked_list = LinkedList()
linked_list.append(12)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(4)
linked_list.append(19)
linked_list.append(26)

print("Linked List elements:")
linked_list.display()

i = 2  # Find the 2nd smallest element
result = ith_order_statistic(linked_list.head, i)
print(f"The {i+1}th smallest element is: {result}")
