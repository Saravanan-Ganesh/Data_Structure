##Queue

from collections import deque

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

a=Queue()
a.enqueue({'company':'google',
           'timestamp':'12 apr , 11.01 AM',
           'price':350})
a.enqueue({'company':'google',
           'timestamp':'13 apr , 11.02 AM',
           'price':820})
a.enqueue({'company':'google',
           'timestamp':'14 apr , 11.03 AM',
           'price':990})

print(a.buffer)
