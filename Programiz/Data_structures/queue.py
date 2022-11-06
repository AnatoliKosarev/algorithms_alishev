class Queue:
    EMPTY_MESSAGE = 'Queue is empty'
    FULL_MESSAGE = 'Queue is full'

    def __init__(self, capacity):
        self.arr = []
        self._capacity = capacity

    def __repr__(self):
        return f"<{', '.join(str(v) for v in self.arr)}>"

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return self._capacity <= 0

    def peek(self):
        if self.is_empty():
            print(self.EMPTY_MESSAGE)
            return

        return self.arr[0]

    # Add element to the end of the queue
    def enqueue(self, element):
        if self.is_full():
            print(self.FULL_MESSAGE)
            return

        self.arr.append(element)
        self._capacity -= 1

    # Remove element from the front of the queue
    def dequeue(self):
        if self.is_empty():
            print(self.EMPTY_MESSAGE)
            return

        result = self.arr.pop(0)
        self._capacity += 1
        return result


queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print(queue.peek())

print(queue._capacity)

print(queue.dequeue())

print("\nAfter dequeue")

print(queue)
print(queue._capacity)
