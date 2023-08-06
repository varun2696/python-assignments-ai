# 5. **Implement Queue using Stack**: Use Python's stack data structure to implement a queue.
#     - *Input*: enqueue(1), enqueue(2), dequeue(), enqueue(3), dequeue(), dequeue()
#     - *Output*: "1, None, 3, None, None"


class QueueUsingStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack:
            if not self.enqueue_stack:
                return None
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()


# Test the queue implementation
queue = QueueUsingStacks()

output = []
queue.enqueue(1)
queue.enqueue(2)
output.append(str(queue.dequeue()))
queue.enqueue(3)
output.append(str(queue.dequeue()))
output.append(str(queue.dequeue()))

print(", ".join(output))
