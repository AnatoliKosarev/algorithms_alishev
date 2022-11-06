
class Stack:

    def __init__(self, capacity):
        self.arr = []
        self.capacity = capacity

    def __repr__(self):
        return f"<{', '.join(str(v) for v in self.arr)}>"

    def is_empty(self):
        return len(self.arr) == 0

    def is_full(self):
        return self.capacity <= 0

    def peek(self):
        if self.is_empty():
            print('Stack is empty')
            return

        return self.arr[-1]

    def push(self, element):
        if self.is_full():
            print('Stack is already full')
            return

        self.arr.append(element)
        self.capacity -= 1
    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return

        result = self.arr.pop()
        self.capacity += 1
        return result


stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

print(stack.peek())

print(stack.pop())

print("\nAfter popping out")

print(stack)
