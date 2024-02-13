class Queue:
    def __init__(self, initial_queue):
        self.queue = initial_queue

    def head_pop(self):
        return self.queue.pop(0)

    def head_push(self, x):
        self.queue = [x] + self.queue

    def append(self, x):
        self.queue.append(x)

    def __getitem__(self, item):
        if type(item) is int:
            return self.queue[item]
        else:
            raise Exception(f"Index must be an integer")
