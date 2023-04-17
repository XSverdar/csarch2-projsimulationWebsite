from twosComp import twosComp

def solve(decimal):
    binary = ['0'] # initialize list
    nums = '' # empty string

    if decimal < 0: # input is negative
        decToBin(abs(decimal), binary) # get positive of input
        binary = twosComp(binary)

    else: # input is positive
        decToBin(decimal, binary)
        
    for i in binary:
        nums += str(i)

    return nums # return list as string

def decToBin(num, binary):
    if num >= 1: # to not exceed maximum recursion depth
        decToBin(num//2, binary)
        binary.append(str(num%2))