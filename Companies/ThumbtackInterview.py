'''
// Create data structure
//  -insert integers 0-999 (inclusive) one at a time
// - calculate mean of the integers so far (arithmetic avg)
// - calculate median of integers so far (if numbers are in sorted order, middle number -- if 2 numbers in middle, avg of those two)

// -insert ~10^9 times
// 10Mb of memory on system
// mean/median called <100 times
'''


class MyStructure:
    def __init__(self, maxValue):
        self.summation = 0
        self.count = 0
        self.numbers = [0 for _ in range(maxValue + 1)]  # including the max value

    def insert(self, num):
        self.summation += num
        self.count += 1
        self.numbers[num] += 1

    def mean(self):
        return float(self.summation) / self.count

    def findCum(self, val, cumm):
        for i, cumFreq in enumerate(cumm):
            if val <= cumFreq:
                return i

    def median(self):
        total = 0
        cumm = []
        for freq in self.numbers:
            cumm.append(total+freq)
            total+=freq
        if self.count % 2 == 1:
            # odd case
            medianFreq = float(self.count) / 2
            return self.findCum(medianFreq, cumm)
        else:
            # even case
            median1 = self.findCum((self.count / 2), cumm)
            median2 = self.findCum((self.count / 2)+1, cumm)
            return float(median1 + median2) / 2


MS = MyStructure(2)
MS.insert(0)
MS.insert(0)
MS.insert(0)
MS.insert(1)
MS.insert(1)
MS.insert(2)
print MS.mean()
print MS.median()
