
class Node:
    """
    A node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A singly linked list implementation.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")
        if position == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current_node = self.head
        current_pos = 0
        while current_node and current_pos < position - 1:
            current_node = current_node.next
            current_pos += 1
        if current_node is None:
            raise IndexError("Position is out of bounds.")
        new_node.next = current_node.next
        current_node.next = new_node

    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return True
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return False
        prev_node.next = current_node.next
        current_node = None
        return True

    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")
        if self.is_empty():
            raise IndexError("List is empty.")
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            current_node = None
            return True
        prev_node = None
        current_pos = 0
        while current_node and current_pos < position:
            prev_node = current_node
            current_node = current_node.next
            current_pos += 1
        if current_node is None:
            raise IndexError("Position is out of bounds.")
        prev_node.next = current_node.next
        current_node = None
        return True

    def delete_all(self, data):
        current_node = self.head
        deleted = False
        while current_node:
            if current_node.data == data:
                deleted = True
                if current_node == self.head:
                    self.head = current_node.next
                    current_node = self.head
                else:
                    prev_node = self.head
                    while prev_node.next != current_node:
                        prev_node = prev_node.next
                    prev_node.next = current_node.next
                    current_node = prev_node.next
            else:
                current_node = current_node.next
        return deleted

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self):
        return self.display()

    def display(self):
        if self.is_empty():
            return "Empty List"
        current_node = self.head
        result = []
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(result)

    def clear(self):
        self.head = None
        return "List cleared."

    def to_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def from_list(self, data_list):
        for data in data_list:
            self.append(data)
        return self

    def sort(self):
        if self.is_empty() or self.head.next is None:
            return
        sorted = False
        while not sorted:
            sorted = True
            current_node = self.head
            while current_node and current_node.next:
                if current_node.data > current_node.next.data:
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                    sorted = False
                current_node = current_node.next

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

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
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.insert_at_position(15, 2)
print("Linked List:", ll.display())
print("Middle Element:", ll.get_middle())
ll.sort()
print("Sorted List:", ll)
ll.reverse()
print("Reversed List:", ll)
ll.delete(20)    
print("After Deletion:", ll)
print("List to Python list:", ll.to_list())
print("Length:", len(ll))
ll.clear()
print("After Clear:", ll)
"""