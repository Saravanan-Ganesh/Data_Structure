##Queue - FIFO
stock_price_queue =[]

stock_price_queue.insert(1,131.10)
stock_price_queue.insert(2,132)
stock_price_queue.insert(3,134.77)
stock_price_queue.insert(4,135.09)

stock_price_queue.pop()
stock_price_queue.pop()

stock_price_queue.pop()
stock_price_queue.pop()

from collections import deque
q=deque()
q.appendleft(5)
q.appendleft(109)
q.appendleft(23)
q.appendleft(990)
print(q)
q.pop()
print(q)
