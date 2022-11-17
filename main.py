# Queue with stack problem
# The aim is to design a queue abstract data type with the help of stacks.

class Queue:

    def __init__(self):
        self.enqueueStack = []
        self.dequeStack = []

    # enqueue function to add items
    def enqueue(self, data):
        self.enqueueStack.append(data)

    # deque function to remove items
    def dequeue(self):
        if len(self.enqueueStack) == 0 and len(self.dequeStack) == 0:
            return "No item to remove"
            # raise Exception("stacks are empty")
        if len(self.dequeStack) == 0:
            while len(self.enqueueStack) > 0:
                self.dequeStack.append(self.enqueueStack[-1])
                del self.enqueueStack[-1]

        removed_item = self.dequeStack[-1]
        del self.dequeStack[-1]
        return f"removed item is {removed_item}"

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(70)
queue.enqueue(80)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(70)
queue.enqueue(80)
print(queue.dequeue())
