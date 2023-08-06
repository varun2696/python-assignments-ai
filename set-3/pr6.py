# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"



from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop()
        return None

    def is_empty(self):
        return len(self.queue) == 0

# Test the stack implementation
stack = Stack()

output = []
stack.push(1)
stack.push(2)
output.append(str(stack.pop()))
stack.push(3)
output.append(str(stack.pop()))
output.append(str(stack.pop()))

print(", ".join(output))
