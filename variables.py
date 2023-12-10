input='''Time:        49     87     78     95
Distance:   356   1378   1502   1882'''

from functools import reduce
from operator import mul

class Race:
    def __init__(self, input) -> None:
        self.lineList = input.split("\n")
        self.time = [int(''.join(self.lineList[0].split(':')[1].strip().split()))]
        self.distance = [int(''.join(self.lineList[1].split(':')[1].strip().split()))]
        self.ways = []
        
    def getWays(self) -> int:
        for i in range(len(self.time)):
            ways = 0
            for k in range(self.time[i]):
                if k * (self.time[i] - k) > self.distance[i]:
                    ways += 1
            self.ways.append(ways)
        return self.ways[0]


