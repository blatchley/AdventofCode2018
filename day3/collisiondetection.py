import numpy as np

canvas = np.zeros((999,999))

with open('input.txt', "r") as f:
        for line in f:
            contents = line.split()
            elvenum = contents[0]
            atsymbol = contents[1]
            coords = contents[2][0:-1].split(",")
            xcoord = int(coords[0])
            ycoord = int(coords[1])
            size = contents[3].split("x")
            sizex = int(size[0])
            sizey = int(size[1])
            for i in range(0,sizex):
                    canvas[xcoord + i, ycoord] += 1
                    canvas[xcoord + i, ycoord + sizey] += -1

sharedElements = 0

for i in range(0,999):
    state = 0
    line = canvas[i]
    for element in line:
        state += element
        if state > 1:
            sharedElements += 1

print(sharedElements)

            
          