class MedianFinder:

    def __init__(self):
        self.mins = []
        self.maxs = []

    def addNum(self, num: int) -> None:
        if len(self.mins) == len(self.maxs):
            heappush(self.maxs, -heappushpop(self.mins, -num))
        else:
            heappush(self.mins, -heappushpop(self.maxs, num))

    def findMedian(self) -> float:
        if len(self.mins) == len(self.maxs):
            return (-self.mins[0] + self.maxs[0])/2
        else:
            return self.maxs[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
