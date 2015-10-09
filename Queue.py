from Exceptions import ArrayFullError, ArrayEmptyError


class Queue:
    def __init__(self, size):
        if size < 0:
            raise ValueError("Size must be positive")
        self.size = size
        self.the_array = size*[None]
        self.count = self.rear = self.front = 0

    def __len__(self):
        return self.count

    def is_full(self):
        return self.count >= len(self.the_array)

    def is_empty(self):
        return self.count == self.size

    def reset(self):
        self.front = self.rear = self.count = 0

    def append(self, new_item):
        if self.is_full():
            raise ArrayFullError("The queue is full.")
        self.the_array[self.rear] = new_item
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def serve(self):
        if self.is_empty():
            raise ArrayEmptyError("The queue is empty.")
        item = self.the_array[self.front]
        self.front = (self.front + 1) % len(self.the_array)
        self.count -= 1
        return item
