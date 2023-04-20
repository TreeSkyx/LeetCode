class MyQueue:

    def __init__(self):
        self.frnt = []  
        self.bck = []  

    def push(self, x):
        self.bck.append(x)  

    def pop(self):
        self.frontToBack()
        return self.frnt.pop()

    def peek(self):
        self.frontToBack()
        return self.frnt[-1]

    def empty(self):
        return len(self.frnt)+len(self.bck) == 0

    def frontToBack(self):
        if not self.frnt:  
            while self.bck:
                self.frnt.append(self.bck.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
