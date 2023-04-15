 class MyQueue:
    # Since Python doesn't have stacks by default, this uses two lists.
    # The only allowed operations were ones for stacks, which were
    # (with the Python analogue):
    # - push to top (list.append())
    # - peek at top (list[-1])
    # - pop from top (list.pop())
    # - size (len(list))
    # - is empty (list == [], or other formulations)

    def __init__(self):
        self.queue = []
        self.storage = []


    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            temp = self.queue.pop()
            self.storage.append(temp)
        desired = self.queue.pop()
        while self.storage:
            self.queue.append(self.storage.pop())
        return desired


    def peek(self) -> int:
        while len(self.queue) > 1:
            temp = self.queue.pop()
            self.storage.append(temp)
        desired = self.queue[-1]
        while self.storage:
            self.queue.append(self.storage.pop())
        return desired

    def empty(self) -> bool:
        return self.queue == []
