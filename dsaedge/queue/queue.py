class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow - Cannot dequeue from empty queue")
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # Queue becomes empty
            self.rear = None
        print(f"Dequeued: {removed_data}")
        return removed_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data

    def display(self):
        if self.is_empty():
            return "Queue is empty"
        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result) + " -> None"

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
