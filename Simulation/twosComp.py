def twosComp(num):
    foundOne = 0 # boolean
    
    for x in reversed(range(len(num))):
        if num[x] == '1' and foundOne == 0:
            foundOne = 1
        elif num[x] == '1' and foundOne == 1:
            num[x] = '0'
        elif num[x] == '0' and foundOne == 1:
            num[x] = '1'

    return num