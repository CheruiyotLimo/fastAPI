class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def pop(self) -> int:
        while self.stack1:
            top = self.stack1.pop()
            self.stack2.append(top)
        result = self.stack2.pop()
        while self.stack2:
            new_top = self.stack2.pop()
            self.stack1.append(new_top)
        return result

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if not self.stack1:
            return True
        return False

mq = MyQueue()
mq.push(1)
print(mq.pop())
print(mq.stack1)
print(mq.stack2)
print(mq.empty())