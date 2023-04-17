import copy
import sum

def solve(inputA, inputB):
    line = []   #per value at intermediate
    all = []    #per row
    inputC = []
    total_Len = len(inputA) + len(inputB)

    inputB = inputB + '0'

    i = len(inputB) - 2
    j = len(inputB) - 1


    while i >= 0 and j >= -1:
        if inputB[i] == '0' and inputB[j] == '0':
            inputC.insert(0, '0')
            x = len(inputA)-1
            while x >= 0:
                ans = int(inputA[x]) * 0   #multiply
                line.insert(0, ans)
                x-=1
            if line[0] == 0:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 0)
            else:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 1)
            total_Len-=1
        elif inputB[i] == '1' and inputB[j] == '1':
            inputC.insert(0, '0')
            x = len(inputA)-1
            while x >= 0:
                ans = int(inputA[x]) * 0   #multiply
                line.insert(0, ans)
                x-=1
            if line[0] == 0:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 0)
            else:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 1)
            total_Len-=1
        elif inputB[i] == '0' and inputB[j] == '1':
            inputC.insert(0, '+1')
            x = len(inputA)-1
            while x >= 0:
                ans = int(inputA[x]) * 1   #multiply
                line.insert(0, ans)
                x-=1
            if line[0] == 0:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 0)
            else:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 1)
            total_Len-=1
        elif inputB[i] == '1' and inputB[j] == '0':
            inputC.insert(0, '-1')
            foundOne = 0 # boolean
            temp1 = []
            for x in reversed(range(len(inputA))):          #2's complement
                if inputA[x] == '1' and foundOne == 0:
                    foundOne = 1
                    line.insert(0, 1)
                elif inputA[x] == '1' and foundOne == 1:
                    line.insert(0, 0)
                elif inputA[x] == '0' and foundOne == 1:
                    line.insert(0, 1)
                else :
                    line.insert(0, int(inputA[x]))
            if line[0] == 0:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 0)
            else:
                z = 0
                while z < total_Len - len(line):    #sign extend
                    line.insert(0, 1)
            total_Len-=1
        all.append(line)
        line = []
        i-=1
        j-=1
        
        #print here for printing

    cc = copy.deepcopy(all)
    print(*cc,sep = "\n")
    
    
    total_Len = len(inputA) + len(inputB)
   
    j = 0
    while j < len(all):         #append 0's at the end to add the lists
        i = len(all[j])
        while i < total_Len-1:
            all[j].append(0)
            i+=1
        j+=1

    result = sum.solve(all[0], all[1], total_Len)
    i = 2
    while i <= len(all)-1:
        result = sum.solve(all[i], result, total_Len)
        i+=1
    result.pop(0)
    print("\n", result, "   <--Final result")

    b00l = 0
    while b00l == 0:
        a = input("\nWould you like to export the solution to a text file? [Y/N]: ")
        if a == 'Y':
            print("Solution has been exported to Booths.txt")
            file = open("Booths.txt", "w") 
            x = 0
            inputB = inputB[:-1]
            file.write("    ")
            file.write(inputA)
            file.write("\nx  ")
            for item in inputC:
                    file.write("%s" % item)
            file.write("\n---------------\n")
            while x < len(cc):
                for item in cc[x]:
                    file.write("%d" % item)
                x+=1
                file.write("   <--Intermediate # %d" % x) 
                file.write("\n")
            file.write("---------------\n")
            for item in result:
                    file.write("%d" % item)
            file.write("  <--Result")
            file.close
            b00l += 1
        elif a == 'N':
            print("Result not transferred to text file.")
            b00l += 1
        else:
            b00l == 0