import numpy as np



twos = 0
threes = 0
with open('input.txt', "r") as f:
        for line in f:
            counts = np.zeros(26)
            for i in range(0, len(line)-1):
                value = ord(line[i]) - ord("a")
                counts[value] = counts[value] + 1
            if 3 in counts:
                threes += 1
            if 2 in counts:
                twos += 1
result = twos * threes
print(result)            