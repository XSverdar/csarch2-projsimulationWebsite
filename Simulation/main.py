import DecimalToSignedBinary
import pencilAndPaper
import booths
import extendedBooths

def loop():
    x = input("\nWould you like to try again? [Y/N]: ")
    if x == 'Y':
        main()
    elif x == 'N':
        print("Program ended.") 
    elif x != 'Y':
        loop()

def main():
    flag = 0
    binary = {'0','1'}

    # only proceed if user input is valid
    while flag == 0:
        inputType = int(input("Enter input type:\n[1] Decimal\n[2] Binary\n"))
        if inputType == 1 or inputType == 2:
            flag = 1

    if inputType == 1: # Decimal
        num1 = int(input("Enter multiplicand: "))
        num2 = int(input("Enter multiplier: "))
        num1 = DecimalToSignedBinary.solve(num1)
        num2 = DecimalToSignedBinary.solve(num2)

    elif inputType == 2: # Binary
        while flag == 1: # only proceed if user inputs valid binary values
            num1 = input("Enter multiplicand: ")
            num2 = input("Enter multiplier: ")

            if set(num1) == binary and set(num2) == binary:
                flag = 0

    inp1 = input("Choose a method:\n[1] Pencil and Paper\n[2] Booth's\n[3] Extended Booth's\n[4] All of the Above\n")

    if(inp1 == "1"):
        print("\nSELECTED: Pencil and Paper\n")
        pencilAndPaper.solve(num1, num2)
    
    elif(inp1 == "2"):
        print("\nSELECTED: Booth's\n")
        booths.solve(num1, num2)

    elif(inp1 == "3"):
        print("\nSELECTED: Extended Booth's\n")
        extendedBooths.solve(num1, num2)

    elif(inp1 == "4"):
        print("\nSELECTED: All of the Above")
        print("\n======================================\nCurrently Processing: Pencil and Paper\n======================================\n")
        pencilAndPaper.solve(num1, num2)
        print("\n=============================\nCurrently Processing: Booth's\n=============================\n")
        booths.solve(num1, num2)
        print("\n======================================\nCurrently Processing: Extended Booth's\n======================================\n")
        extendedBooths.solve(num1, num2)
    
    loop()
main()