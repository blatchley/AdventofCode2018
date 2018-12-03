import numpy as np



def compareLabels(string1, string2):
    errors = 0
    illegalIndex = 0
    for i in range(0, len(string1)-1):
        if string1[i] != string2[i]:
            errors += 1
            if errors > 1:
                return 
            else:
                illegalIndex = i
                
    newstr = string1[:illegalIndex] + string1[illegalIndex+1:]
    print(newstr)
    return 

labelList = []

with open('input.txt', "r") as f:
    ##should probably terminate when correct answer found, but not needed as dataset is small
        for line in f:
            for string in labelList:
                compareLabels(line, string)      
            labelList.append(line)
