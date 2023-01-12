# Queue can be implemented using
# 1. Lists (Can refer to arrays they are almost the same)
# 2. Deque
# 3. Queue

# |--------------------------|
# |                          |
# |       USING LIST         |
# |                          |
# |--------------------------|
lt = []
lt.append("a")
lt.append("b")
lt.append("c")
print("Initial values")
print(lt)
lt.pop(0)
lt.pop(0)
print("Elements  after popping out elements")
print(lt)

# |--------------------------|
# |                          |
# |       USING DEQUE        |
# |                          |
# |--------------------------|
from collections import deque

deque = deque()
# Add elements using append()
deque.append("a")
deque.append("b")
deque.append("c")
print("Initial queue")
print(deque)

# Removing Elements from a queue
deque.popleft()
deque.popleft()
print("Elements after popping elements")
print(deque)

# |--------------------------|
# |                          |
# |       USING QUEUE        |
# |                          |
# |--------------------------|

from queue import Queue
q = Queue()
# add elements using Put()
q.put("a")
q.put("b")
q.put("c")
print("Initial elements")
print(q.queue)

# Remove elements using get()
q.get()
q.get()
print("Elements after removing some elements")
print(q.queue)

# empty() => shows if queue is empty returns boolean
# full() => shows if queue is full returns boolean
print(f"Shows if queue is empty: => {q.empty()}")
print(f"Shows if queue is full: => {q.full()}")