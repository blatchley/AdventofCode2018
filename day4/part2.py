import numpy as np
import operator
class Guard:
    def __init__(self, id, minutes, totalminutes):
        self.id = id
        self.minutes = minutes
        self.totalminutes = totalminutes

    def sleepsfrom(self, start , to ):
        for i in range(start, to):
            self.minutes[i] += 1
        self.totalminutes += to - start
    
    def sleepiestminute(self):
        return np.max(self.minutes)

    

sleepstart = -1
currentguard = 0
guardlist = {}
with open('input.txt', "r") as f:
    data = f.read().split("\n")
    data.sort()

    for element in data[1:]:
        event = element.split()
        if event[2] == "Guard":
            if sleepstart >= 0:
                guardlist[currentguard].sleepsfrom(sleepstart,60)
                sleepstart = -1
            currentguard = int(event[3][1:])
            if currentguard not in guardlist:
                guardlist[currentguard] = Guard(currentguard, np.zeros(60), 0)
        if event[2] == "falls":
            sleepstart = int(event[1][3:5])
        if event[2] == "wakes":
            sleepend = int(event[1][3:5])
            guardlist[currentguard].sleepsfrom(sleepstart,sleepend)
            sleepstart = -1
        
        
sleepiestguard =  (sorted(guardlist.values(), key=operator.methodcaller("sleepiestminute")))[-1]
result = sleepiestguard.id * (np.argmax(sleepiestguard.minutes))
print(result)



