class Stack:
    def __init__(self):
        self.top = []
    def __len__(self) -> bool:
        return len(self.top)

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print('Stack Underflow')
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print('underflow')
            exit()
    
    def isEmpty(self) -> bool:
        return len(self.top) == 0

    def clear(self):
        self.top = []
    
    def isContain(self, item) -> bool:
        return item in self.top

    def isFull(self) -> bool:
        return self.size() == self.limit

    def size(self) -> int:
        return len(self.top)