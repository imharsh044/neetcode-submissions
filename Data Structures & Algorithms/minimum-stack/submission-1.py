class MinStack:

    def __init__(self):
        self.min_stack = []
        self.head = None
        self.min_num = float('Inf')

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        self.head = len(self.min_stack) - 1
        self.min_num =  min(self.min_num, val)

    def pop(self) -> None:
        if len(self.min_stack) > 0:
            self.min_stack.pop()

        if len(self.min_stack) > 0:
            self.head = len(self.min_stack) - 1
            self.min_num = min(self.min_stack)

    def top(self) -> int:
        return self.min_stack[self.head]

    def getMin(self) -> int:
        return self.min_num
