class MinStack:

    def __init__(self):
        self.storage = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val < self.min_stack[len(self.min_stack)-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        
        self.storage.append(val)
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.storage.pop()
        

    def top(self) -> int:
        return self.storage[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
