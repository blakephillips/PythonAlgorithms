# https://leetcode.com/problems/moving-average-from-data-stream/
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
# ------

# Note: Uses the sliding window approach to avoid interating over the whole list every time a value is added/removed


class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.windowSum = 0
        
        self.head = 0
        self.size = size

    def next(self, val: int) -> float:
        if  len(self.queue) >= self.size:
            self.windowSum -= self.queue.pop(0)
        
        self.queue.append(val)
        self.windowSum += val
        
        return self.windowSum / len(self.queue)

#Tests
if __name__ == '__main__':
    movingAverage = MovingAverage(3)
    print(movingAverage.next(1)) # return 1.0 = 1 / 1
    print(movingAverage.next(10)) # return 5.5 = (1 + 10) / 2
    print(movingAverage.next(3)) # return 4.66667 = (1 + 10 + 3) / 3
    print(movingAverage.next(5)) # return 6.0 = (10 + 3 + 5) / 3
    print(f"test = {1 + -1}")