from twosComp import twosComp
import BinaryToDecimal
import DecimalToSignedBinary

def multiply(answer,alignCounter,bits):
    for z in range(alignCounter):
        answer.append('0')
        answer.append('0')
    for w in range(len(answer),bits):
        answer.insert(0,answer[0])

    return answer.copy()

def solve(num1,num2):
    # assume binary
    num1 = list(num1)
    num2 = list(num2)

    # number of bits required
    bits = len(num1)+len(num2)

    if len(num2) % 2 != 0: # multiplier has odd number of bits
        num2.insert(0,num2[0]) # sign-extend

    num2.append('0') # append 0 to end of multiplier

    # ------------------- #

    # trio variables
    counter = 0
    trio = [0] * 3

    # result array
    num2result = []

    # cases
    case000 = ['0','0','0'] # 0
    case001 = ['0','0','1'] # +1
    case010 = ['0','1','0'] # +1
    case011 = ['0','1','1'] # +2
    case100 = ['1','0','0'] # -2
    case101 = ['1','0','1'] # -1
    case110 = ['1','1','0'] # -1
    case111 = ['1','1','1'] # 0

    for x in range(len(num2)+1):
        if counter < 3:
            trio[counter] = num2[x]
            counter += 1
        else: # bit-pair recording
            if trio == case000:
                num2result.append('0')
            elif trio == case001:
                num2result.append('1')
            elif trio == case010:
                num2result.append('1')
            elif trio == case011:
                num2result.append('2')
            elif trio == case100:
                num2result.append('-2')
            elif trio == case101:
                num2result.append('-1')
            elif trio == case110:
                num2result.append('-1')
            elif trio == case111:
                num2result.append('0')

            if x < len(num2)-1:
                trio[0] = num2[x-1]
                trio[1] = num2[x]
                counter = 2

    # ------------------- #

    # multiplication variables
    alignCounter = 0
    answer = []
    result = [['0'] * bits] * len(num2result)

    # multiplication process
    for x in reversed(range(len(num2result))):
        if alignCounter < len(num2result):
            if num2result[x] == '0':
                alignCounter += 1

            elif num2result[x] == '1':
                answer = num1.copy()

                result[alignCounter] = multiply(answer,alignCounter,bits)
                answer.clear()
                alignCounter += 1

            elif num2result[x] == '2':
                answer = num1.copy()
                answer.append('0')

                result[alignCounter] = multiply(answer,alignCounter,bits)
                answer.clear()
                alignCounter += 1

            elif num2result[x] == '-1':
                answer = num1.copy()
                answer = twosComp(answer)

                result[alignCounter] = multiply(answer,alignCounter,bits)
                answer.clear()
                alignCounter += 1

            elif num2result[x] == '-2':
                answer = num1.copy()
                answer.append('0')
                answer = twosComp(answer)

                result[alignCounter] = multiply(answer,alignCounter,bits)
                answer.clear()
                alignCounter += 1

    # add result of multiplication
    sum = 0

    for x in range(len(num2result)):
        sum += BinaryToDecimal.solve(result[x])

    finalAnswer = list(DecimalToSignedBinary.solve(sum))

    # sign-extend
    for x in range(len(finalAnswer),bits):
        finalAnswer.insert(0,finalAnswer[0])

    # combine list into a string
    combined = ''
    for x in finalAnswer:
        combined += x

    # ------------------- #

    # text file variables
    resultcopy = result.copy()
    number = 1
    number2 = 1
    counter2 = 0
    resultCombined = ''
    flag = 0

    # cut zeroes from matrix so text file will look cleaner
    for x in range(len(num2result)):
        if counter2 == 0:
            counter2 += 1
        else:
            for y in range(bits-(counter2*2),bits):
                resultcopy[x][y] = ' '
                counter2 += 1

    print(num1)
    print(num2)
    print("--------------")
    for x in resultcopy:
        print(x, " <-- Intermediate # ",number2)
        number2 += 1
    print("--------------")
    print(finalAnswer, " <-- Final Result")

    while flag == 0:
        textfileprompt = input("\nWould you like to export the solution to a text file? [Y/N]: ")
        if textfileprompt == 'Y':
            print("Solution has been exported to extendedBooths.txt")
            flag = 1

            # write text file
            with open('extendedBooths.txt','w') as f:
                f.write('  ')
                f.writelines(num1)
                f.write('\n')
                f.write('x ')
                #f.writelines(num2result)
                for x in num2result:
                    if x == '1':
                        f.write('+1')
                    elif x == '2':
                        f.write('+2')
                    else:
                        f.write(x)
                f.write('\n')
                f.write('---------------------')
                f.write('\n')
                for elem in resultcopy:
                    for y in elem:
                        resultCombined += str(y)
                    f.write(resultCombined)
                    resultCombined = ''
                    f.write('  <---- Intermediate # ')
                    f.write(str(number))
                    number += 1
                    f.write('\n')
                f.write('---------------------')
                f.write('\n')
                f.write(combined)
                f.write('  <---- Result')
        elif textfileprompt == 'N':
            print("Result not transferred to text file.")
            flag = 1

    return combined
