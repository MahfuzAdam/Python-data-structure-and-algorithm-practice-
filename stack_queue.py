class Stack:
    def __init__(self):
        self.items = []
    def push(self, x): self.items.append(x)
    def pop(self): return self.items.pop() if self.items else None
    def peek(self): return self.items[-1] if self.items else None

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, x): self.items.append(x)
    def dequeue(self): return self.items.pop(0) if self.items else None