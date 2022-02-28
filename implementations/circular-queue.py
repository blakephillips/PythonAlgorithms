#Implementation of a circular queue

from typing import List

class CircularQueue:
        
    def __init__(self, k: int):
        
        #Queue length
        self.length = k

        #Initialize list/arr
        self.queue = [None] * k

        #Head / tail index pointers
        self.head = -1
        self.tail = -1
    
    #Add integer to the queue, return success
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        
        if self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = self._MovePointer(self.tail)
    
        self.queue[self.tail] = value
        

        return True
    
    #Remove from the queue, return success
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        
        self.queue[self.head] = None
        
        #Dequeuing the last object (empty)
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = self._MovePointer(self.head)
        return True
        
    #Get the variable off the front of the queue
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.head]

    #Get the variable off the end of the queue
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.queue[self.tail]

    #Determine if the queue is empty
    def isEmpty(self) -> bool:
        return self.head == -1 and self.tail == -1

    #Determine if the queue is full
    def isFull(self) -> bool:
        return not self.isEmpty() and self._MovePointer(self.tail) == self.head
    
    #Move pointer (head, or tail) positively or negatively by 1, handling wrapping (end wraps to front, front wraps to end)
    def _MovePointer(self, pos : int, positive : bool = True) -> int:
        if positive: 
            if (pos + 1) >= self.length: 
                return 0
            return pos + 1
        
        if not positive:
            if (pos - 1) <= -1:
                return self.length - 1
            return pos - 1

#Tests
if __name__ == '__main__':
    myCircularQueue = CircularQueue(3)
    print(myCircularQueue.enQueue(1)) # return True
    print(myCircularQueue.enQueue(2)) # return True
    print(myCircularQueue.enQueue(3)) # return True
    print(myCircularQueue.enQueue(4)) # return False
    print(myCircularQueue.Rear())     # return 3
    print(myCircularQueue.isFull())   # return True
    print(myCircularQueue.deQueue())  # return True
    print(myCircularQueue.enQueue(4)) # return True
    print(myCircularQueue.Rear())     # return 4