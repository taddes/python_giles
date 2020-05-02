class Stack:
    def __init__(self, data=[]):
        self.data = data
    
    def peek(self):
        return self.data[len(self.data)-1]

    def pop(self):
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def __repr__(self):
        return repr(self.data)


staq = Stack()
print(staq.data)
staq.push(2)
print(staq.data)
staq.push(3)
print(staq.data)
print(staq.peek())
staq.pop()
staq.push(4)
staq.push(5)
print(staq.data)
print(staq.peek())
print(staq)