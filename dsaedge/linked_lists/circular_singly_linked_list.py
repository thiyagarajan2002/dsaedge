class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    """
    A circular singly linked list implementation.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_position(self, data, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")
        if position == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        current_pos = 0

        while current and current_pos < position - 1:
            current = current.next
            current_pos += 1

        if current is None or (current.next == self.head and current_pos < position - 1):
            raise IndexError("Position is out of bounds.")

        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if self.is_empty():
            return False

        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return True

        current = self.head
        prev = None

        while True:
            prev = current
            current = current.next
            if current.data == data:
                prev.next = current.next
                return True
            if current == self.head:
                break
        return False

    def delete_at_position(self, position):
        if position < 0:
            raise IndexError("Position cannot be negative.")
        if self.is_empty():
            raise IndexError("List is empty.")
        if position == 0:
            return self.delete(self.head.data)

        current = self.head
        prev = None
        current_pos = 0

        while current and current_pos < position:
            prev = current
            current = current.next
            current_pos += 1

        if current is None or (current == self.head and current_pos < position):
            raise IndexError("Position is out of bounds.")

        prev.next = current.next
        return True

    def delete_all(self, data):
        if self.is_empty():
            return False

        deleted = False
        current = self.head
        prev = None

        while True:
            next_node = current.next
            if current.data == data:
                deleted = True
                if current == self.head:
                    if self.head.next == self.head:
                        self.head = None
                        return True
                    else:
                        last = self.head
                        while last.next != self.head:
                            last = last.next
                        self.head = self.head.next
                        last.next = self.head
                        current = self.head
                        if current.data != data:
                            prev = current
                else:
                    prev.next = current.next
                    current = prev.next
                    if current == self.head:
                        break
                    continue
            else:
                prev = current
                current = next_node
                if current == self.head:
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
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def __str__(self):
        if self.is_empty():
            return "Empty List"
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(nodes) + " -> (head)"

    def display(self):
        if self.is_empty():
            return "Empty List"
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(nodes) + " (circular)"

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
        return "List created from Python list."

    def sort(self):
        if self.is_empty() or self.head.next == self.head:
            return
        sorted = False
        while not sorted:
            sorted = True
            current = self.head
            while True:
                next_node = current.next
                if next_node == self.head:
                    break
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    sorted = False
                current = next_node
        return "List sorted."

    def reverse(self):
        if self.is_empty() or self.head.next == self.head:
            return
        prev = None
        current = self.head
        first = self.head
        while True:
            next_node = current.next
            current.next = prev if prev else first
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head = prev
        return "List reversed."

    def get_middle(self):
        if self.is_empty():
            return None
        slow = self.head
        fast = self.head
        while True:
            fast = fast.next.next if fast.next and fast.next != self.head else None
            slow = slow.next
            if fast == self.head or (fast and fast.next == self.head):
                break
        return slow.data if slow else None

    def __iter__(self):
        if self.is_empty():
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    


"""
cll = CircularSinglyLinkedList()
cll.from_list([3, 1, 4, 1, 5, 9, 2])
print("Original:", cll.display())

cll.sort()
print("Sorted:", cll.display())

cll.reverse()
print("Reversed:", cll.display())

print("Middle Element:", cll.get_middle())

cll.delete_all(1)
print("After deleting all 1s:", cll.display())
"""