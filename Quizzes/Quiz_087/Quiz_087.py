class Stack:
    def __init__(self):
        self.data = QUEUE()
    def push(self, item):
        self.data.enqueue(item)
    def pop(self):
        copy = QUEUE()
        while True:
            item = self.data.dequeue()
            if self .data.isEmpty():
                self.data = copy
                return item
            else:
                copy.enqueue(item)
    def isEmpty(self):
        return self.data.isEmpty()










