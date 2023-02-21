#!/usr/bin/env python3
"""
program_name.py
*insert description*
"""

__author__ = "Julian Harrison"
__version__ = "insert date"


class Stack(object):
    def __init__(self):
        self.stuff = []
    
    def push(self, item):
        self.stuff.append(item)
    
    def pop(self):
        return self.stuff.pop()
    
    def peek(self):
        return self.stuff[-1]
    
    def size(self):
        return len(self.stuff)
    
    def isEmpty(self):
        return len(self.stuff) == 0

class Queue(object):
    def __init__(self):
        self.q = []
    
    def enqueue(self,item):
        self.q.append(item)
    
    def dequeue(self):
        return self.q.pop(0)
    
    def peek(self):
        return self.q[0]
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return len(self.q)==0
    
    def __str__(self):
        return "Queue" + str(self.q) 

class Deque(object):
    def __init__(self):
        self.dq = []
    
    def addFront(self,item):
        return self.dq.insert(0,item)
    
    def addRear(self,item):
        return self.dq.append(item)
    
    def removeFront(self):
        return self.dq.pop(0)
    
    def removeRear(self):
        return self.dq.pop(len(self.dq)-1)
    
    def size(self):
        return len(self.dq)
    
    def isEmpty(self):
        return len(self.dq)==0





if __name__ == "__main__":
    main()