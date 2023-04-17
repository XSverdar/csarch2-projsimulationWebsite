import copy
import sum

def solve(inputA, inputB):
    total_Len = len(inputA) + len(inputB)   #length of intermediate
    
    j = len(inputB)-1
    line = []   #per value at intermediate
    all = []    #per row
    copy1 = []
    while j >= 0:
        i = len(inputA)-1
        while i >= 0:
            ans = int(inputA[i]) * int(inputB[j])   #multiply
            line.insert(0, ans)
            i-=1
        if line[0] == 0:
            z = 0
            while z < total_Len - len(line):    #sign extend
                line.insert(0, 0)
        else:
            z = 0
            while z < total_Len - len(line):    #sign extend
                line.insert(0, 1)
        total_Len -= 1      #to shift left 1 bit
        all.append(line)
        line = []  
        j-=1

    copy1 = copy.deepcopy(all)  #make duplicate (for printing)....NOT WORKING

    total_Len = len(inputA) + len(inputB)

    print(*all, sep = "\n")

    if inputB[0] == "1":
        foundOne = 0 # boolean
        temp1 = []
        for x in reversed(range(len(inputA))):          #2's complement
            if inputA[x] == '1' and foundOne == 0:
                foundOne = 1
                temp1.insert(0, 1)
            elif inputA[x] == '1' and foundOne == 1:
                temp1.insert(0, 0)
            elif inputA[x] == '0' and foundOne == 1:
                temp1.insert(0, 1)
            else :
                temp1.insert(0, int(inputA[x]))
        lengt = len(temp1)
        copy2 = copy.deepcopy(temp1)   #make dupe
        while lengt < total_Len:    #append 0's at the end to add the lists
            temp1.append(0)
            lengt+=1

    j = 0
    while j < len(all):         #append 0's at the end to add the lists
        i = len(all[j])
        while i < total_Len:
            all[j].append(0)
            i+=1
        j+=1      
    
    
    if inputB[0]=='1':
        print(copy2, "                   <-- 2's complement of multiplicand")

   
    
    #Add them all together:
    result = sum.solve(all[0], all[1], total_Len)
    i = 2
    while i <= len(all)-1:
        result = sum.solve(all[i], result, total_Len)
        i+=1
    if inputB[0]=='1':
        result = sum.solve(temp1, result, total_Len)
    print("\n", result, "   <--Final result")

    b00l = 0
    while b00l == 0:
        a = input("\nWould you like to export the solution to a text file? [Y/N]: ")
        if a == 'Y':
            print("Solution has been exported to PencilAndPaper.txt")
            file = open("PencilAndPaper.txt", "w") 
            x = 0
            y = 0
            file.write("    ")
            file.write(inputA)
            file.write("\nx  ")
            file.write(inputB)
            file.write("\n---------------\n")
            while x < len(copy1):
                for item in copy1[x]:
                    file.write("%d" % item)
                x+=1
                file.write("   <--Intermediate # %d" % x) 
                file.write("\n")
            if inputB[0]=='1':
                for item in copy2:
                    file.write("%d" % item)
                file.write("   <--2's complement of multiplicand")
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