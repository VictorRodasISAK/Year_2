class Container:
    def __init__(self):
        self.data = []

    def get(self):
        return self.data[0]

    def set(self,x):
        self.data[0] = x

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        C = Container()
        C.set(x)
        self.queue.append(C)

    def is_empty(self):
        if len(self.queue) != 0:
            return False

    def dequeue(self):
        if self.is_empty():
            return self.queue.pop(0).get()
        return None


