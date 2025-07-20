class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    A doubly linked list implementation.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")
        if position == 0:
            self.prepend(data)
            return

        current = self.head
        index = 0
        while current and index < position:
            current = current.next
            index += 1

        if current is None and index < position:
            raise IndexError("Position is out of bounds.")

        if current is None:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
            if new_node.prev is None:
                self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return True
            current = current.next
        return False

    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")
        current = self.head
        index = 0
        while current and index < position:
            current = current.next
            index += 1
        if current is None:
            raise IndexError("Position is out of bounds.")

        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        return True

    def delete_all(self, data):
        current = self.head
        deleted = False
        while current:
            next_node = current.next
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                deleted = True
            current = next_node
        return deleted

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        if self.is_empty():
            return "Empty List"
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " <-> ".join(result)

    def display(self):
        if self.is_empty():
            print("Empty List")
        else:
            print("List:", self)
            print("Head:", self.head.data)
            print("Tail:", self.tail.data)
            print("Size:", len(self))
            print("Is Empty:", self.is_empty())

    def clear(self):
        self.head = None
        self.tail = None
        print("List cleared.")

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def from_list(self, data_list):
        self.clear()
        for data in data_list:
            self.append(data)
        return "List created from Python list."

    def sort(self):
        if self.is_empty() or self.head == self.tail:
            return "List is empty or has only one element, no sorting needed."

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next
        return "List sorted."

    def reverse(self):
        if self.is_empty():
            return "List is empty, nothing to reverse."

        current = self.head
        self.tail = current
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev
        return "List reversed."

    def get_middle(self):
        if self.is_empty():
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

"""
dll = DoublyLinkedList()
dll.from_list([10, 5, 20, 15])
print("Original:", dll)

dll.sort()
print("Sorted:", dll)

dll.reverse()
print("Reversed:", dll)

print("Middle Element:", dll.get_middle())

dll.delete_all(5)
print("After deleting 5s:", dll)

dll.insert_at_position(99, 1)
print("After inserting 99 at position 1:", dll)

dll.display()
"""