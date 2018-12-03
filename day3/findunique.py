import numpy as np

canvas = np.zeros((999,999))

with open('input.txt', "r") as f:
        for line in f:
            contents = line.split()
            coords = contents[2][0:-1].split(",")
            xcoord = int(coords[0])
            ycoord = int(coords[1])
            size = contents[3].split("x")
            sizex = int(size[0])
            sizey = int(size[1])
            for i in range(0,sizex):
                    canvas[xcoord + i, ycoord] += 1
                    canvas[xcoord + i, ycoord + sizey] += -1

        for i in range(0,999):
            state = 0
            for j in range(0,999):
                state += canvas[i,j]
                canvas[i,j] = state
                
##no need to reload file        
with open('input.txt', "r") as f:
    for line in f:
        correctelf = True
        contents = line.split()
        elvenum = contents[0]
        coords = contents[2][0:-1].split(",")
        xcoord = int(coords[0])
        ycoord = int(coords[1])
        size = contents[3].split("x")
        sizex = int(size[0])
        sizey = int(size[1])
        for i in range(0,sizex):
            for j in range(0,sizey):
                if canvas[xcoord + i, ycoord + j] > 1:
                    correctelf = False
                    
        if correctelf == True:
            print(elvenum)



            
          