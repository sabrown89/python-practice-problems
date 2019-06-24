class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)
