# Stack is a linear data structure that stores items in a Last in/First out (LIFO) or (First in Last Out)
from collections import deque

stack = []
# Append function to push
stack.append("a")
stack.append("b")
stack.append("c")
print("Out put after appending Items")
print(stack)

# Pop function removes elements from the last element of the stack to the first
stack.pop()
stack.pop()
print("Elements in the stack after some elements being popped")
print(stack)

# |_____________________________________|
# |                                     |
# |          USING DEQUE                |
# |                                     |
# |_____________________________________|

stack = deque()

# push using append method
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial stack of deque")
print(stack)

# Remove elements by using pop
stack.pop()
stack.pop()
print("Stack after popping out some elements")
print(stack)

# |_____________________________________|
# |                                     |
# |     USING QUEUE MODULE              |
# |                                     |
# |_____________________________________|

from queue import LifoQueue

stack = LifoQueue(maxsize=4)

# QSize show the number of Elements in the stack
print(f"number of elements in the stack: {stack.qsize()} ")

# put() is used to push elements in the stack
stack.put("a")
stack.put("b")
stack.put("c")
print(stack.queue)

# get() removes elements from stack

stack.get()
stack.get()
print("Elements after using get() method to remove elements")
print(stack.queue)

print(f"Show if it is full: {stack.full()}")  # Returns boolean
print(f"Show if it is empty: {stack.empty()}")  # Returns boolean
