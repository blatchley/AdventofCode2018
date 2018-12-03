valuelist = [0]
value = 0
notFound = True
##really slow, should probably redo this at some point.
while notFound:
    print(len(valuelist))
    with open('input.txt', "r") as f:
        for line in f:
            linevalue = int(line)
            value += linevalue
            if value in valuelist:
                print(value)
                notFound = False
                break
            else:
                valuelist.append(value)

    
            