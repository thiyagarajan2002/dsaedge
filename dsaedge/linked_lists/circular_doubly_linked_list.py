class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        self.append(data)
        self.head = self.head.prev

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Negative position is invalid.")
        if position == 0 or self.is_empty():
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        index = 0
        while index < position - 1 and current.next != self.head:
            current = current.next
            index += 1

        if index != position - 1:
            raise IndexError("Position out of bounds.")

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    def delete(self, data):
        if self.is_empty():
            return False

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:  # only one node
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def delete_at_position(self, position):
        if self.is_empty():
            raise IndexError("List is empty.")
        if position < 0:
            raise IndexError("Negative position is invalid.")

        current = self.head
        index = 0

        if position == 0:
            if current.next == current:
                self.head = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.head = current.next
            return True

        while index < position and current.next != self.head:
            current = current.next
            index += 1

        if index != position:
            raise IndexError("Position out of bounds.")

        current.prev.next = current.next
        current.next.prev = current.prev
        return True

    def delete_all(self, data):
        if self.is_empty():
            return False

        current = self.head
        deleted = False

        while True:
            next_node = current.next
            if current.data == data:
                if current.next == current:
                    self.head = None
                    return True
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = next_node
                    deleted = True
            current = next_node
            if current == self.head or self.head is None:
                break
        return deleted

    def search(self, data):
        if self.is_empty():
            return None
        current = self.head
        while True:
            if current.data == data:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def __len__(self):
        if self.is_empty():
            return 0
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count

    def display(self):
        if self.is_empty():
            return "Empty List"
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " <-> ".join(elements)

    def reverse(self):
        if self.is_empty():
            return
        current = self.head
        while True:
            current.prev, current.next = current.next, current.prev
            current = current.prev
            if current == self.head:
                break
        self.head = self.head.next

    def clear(self):
        self.head = None

    def to_list(self):
        if self.is_empty():
            return []
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def from_list(self, data_list):
        self.clear()
        for data in data_list:
            self.append(data)

    def sort(self, reverse=False):
        if self.is_empty() or self.head.next == self.head:
            return

        # Convert to list, sort, then rebuild
        sorted_data = sorted(self.to_list(), reverse=reverse)
        self.clear()
        for data in sorted_data:
            self.append(data)

"""
cdll = CircularDoublyLinkedList()
cdll.append(10)
cdll.append(20)
cdll.append(30)
print("List:", cdll.display())         # 10 <-> 20 <-> 30
cdll.prepend(5)
print("After prepend:", cdll.display())  # 5 <-> 10 <-> 20 <-> 30
cdll.insert_at_position(15, 2)
print("Insert 15 at position 2:", cdll.display())  # 5 <-> 10 <-> 15 <-> 20 <-> 30
cdll.delete(10)
print("After deleting 10:", cdll.display())  # 5 <-> 15 <-> 20 <-> 30
cdll.reverse()
print("After reverse:", cdll.display())  # 30 <-> 20 <-> 15 <-> 5
print("Length:", len(cdll))  # 4
print("To List:", cdll.to_list())  # [30, 20, 15, 5]
cdll.clear()
print("After clearing:", cdll.display())  # Empty List

cdll.from_list([30, 10, 50, 20])
print("Original List:", cdll.display())   # 30 <-> 10 <-> 50 <-> 20

cdll.sort()
print("Sorted List (asc):", cdll.display())  # 10 <-> 20 <-> 30 <-> 50

cdll.sort(reverse=True)
print("Sorted List (desc):", cdll.display())  # 50 <-> 30 <-> 20 <-> 10

"""