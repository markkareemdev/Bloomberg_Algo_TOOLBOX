from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.d = defaultdict(lambda: (0, 0))
        self.trip = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None: 
        self.trip[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.trip[id]
        totalTime, trips = self.d[(startStation, stationName)] 
        self.d[(startStation, stationName)] = (totalTime + (t - startTime), trips + 1)
        #del self.trip[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, trips = self.d[(startStation, endStation)]
        return totalTime / trips


import collections
class UndergroundSystem:

    def __init__(self):
        self.checkIns = collections.defaultdict(list)
        self.locations = collections.defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        self.locations[(self.checkIns[id][0],stationName)].append(t - self.checkIns[id][1])
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.locations[(startStation,endStation)])/len(self.locations[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)