##Stack - LIFO

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    a=Stack()
    print(reverse_string("World of Programmimg is interesting..."))
    a.push("saro")
    a.push("muke")
    a.push("saru")
    a.push("muke_saru")
    print(a.pop())
    a.push("@!#")
