def signed_binary_addition(a, b, totalLen):
    decA = 0
    decB = 0
    x = totalLen-1
    for i in range(len(a)):
        decA = decA + a[i] * 2 ** (len(a) - i - 1)      #swap to decimal for easier addition
        decB = decB + b[i] * 2 ** (len(b) - i - 1)
    final = decA + decB
    temp1 = []
    if final == 0:
        while x >= 0:
            temp1.append(0) 
            x-=1           #whole row of 0's
    else:
        while final > 0 and len(temp1) < len(a)+len(b):     #check if final has reached end (1 or 2)
            bit = final % 2         #mod2 to get remainder
            temp1.insert(0, bit)
            final = final // 2      #div2 to update final
        temp1 = [0] * (len(a) - len(temp1)) + temp1

    while len(temp1) > totalLen:    #to remove extra bits
        temp1.pop(0)

    return temp1


def solve(a,b, totalLen):
    result = signed_binary_addition(a,b, totalLen)
    return result