#import

#global variables

#function
def print_menu():
    print("===============================")
    print("[1] Sum")
    print("[2] Substract")
    print("[3] Multiplication")
    print("[4] Division")
    print("===============================")

    #plain instructions
    print_menu()
    opt = input("select an option:")
    num1 = float(input("please provide num 1:"))
    num2 = float(input("please provide num 2:"))

    if opt == "1":
        total = num1 + num2
        print ("the total is" + str(total))
    
    elif opt == "2":
        total = num1 - num2
        print ("the total is" + str(total))

    elif opt == "3":
        total = num1 * num2
        print ("the total is" + str(total))

    elif opt == "4":
        if num2 == 0:
            print("Error: don't divide by zero")
        else:
            total = num1 / num2
            print ("the total is" + str(total))


