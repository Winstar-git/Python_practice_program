#Insert all the programs in each fuction

# Prog01: Create a program that ask user to input 2 numbers.
# Print the smaller number.

def Prog01():
    print("Prog01: Create a program that ask user to input 2 numbers.")
    print("        Print the smaller number.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 < num2:
        print(f"{num1} is smaller number.")
    else:
        print(f"{num2} is smaller number.")

# Prog02: Create a program that ask user to input 2 numbers.
# Print "Not Equal" when the numbers are not the same.

def Prog02(): 
    print("Prog02: Create a program that ask user to input 2 numbers.")
    print("        Print 'Not Equal' when the numbers are not the same.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if num1 != num2:
        print(f"{num1} and {num2} are NOt Equal")
    else:
        print(f"{num1} and {num2} are Equal")

# Prog03: Create a program that ask user to input 2 numbers.
# Print the difference of the two numbers.

def Prog03():
    print("Prog03: Create a program that ask user to input 2 numbers.")
    print("        Print the difference of the two numbers.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The difference of {num1} and {num2} is {num1 - num2}")

# Prog04: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers without decimal point.

def Prog04():
    print("Prog04: Create a program that ask user to input 2 numbers.")
    print("        Print the quotient of the two numbers without decimal point.")
    print()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The quotient of the two numbers is: {num1/num2:.0f}" )

# Prog05: Create a program that ask user to input 2 numbers. 
# Print the remainder of the two first number is divided by second number

def Prog05():
    print("Prog05: Create a program that ask user to input 2 numbers.")
    print("        Print the remainder of the two first number is divided by second number")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The remainder of the two numbers is {num1%num2}")   

# Prog06: Create a program that ask user to input 10 numbers. 
# Printthe result of the first number minus all of the remaining numbers.

def Prog06():
    print("Prog06: Create a program that ask user to input 10 numbers.")
    print("        Print the result of the first number minus all of the remaining numbers.")
    print()
    sum = 0
    first = int(input("1. Enter a number: "))
    for i in range(2,11):
        num = int(input(f"{i}. Enter a number: "))
        sum += num
    result = first - sum
    print(f"The result of the first number minus all of the remaining numbers: {result}")

# Prog07: Create a program that ask user to input 10 numbers. 
# Print how many are even numbers.

def Prog07():
    print("Prog07: Create a program that ask user to input 10 numbers.")
    print("        Print how many are even numbers.")
    print()
    count = 0
    for i in range(1,11):
        num = int(input(f"{i}. Enter a number: "))
        if num % 2 == 0:
            count += 1
    print(f"There are {count} even numbers")

#Prog08: Create a program that print all the 
# odd numbers starting from 0 to 100. (Use while loop)

def Prog08():
    print("Prog08: Create a program that print all the ")
    print("        odd numbers starting from 0 to 100. (Use while loop)")
    print()
    num = 1
    while num <= 100:
        print(num, end=" ")
        num += 2

#Prog09: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero or ending five.

def Prog09():
    print("Prog09: Create a program that print all the numbers starting from") 
    print("        0 to 100 except numbers ending in zero or ending five.")
    print()
    for i in range(0,101):
        if i % 5 != 0:
            print(i, end=" ")
    print()

# Prog10: Create a program that ask user to input 2 numbers. 
# Print all the numbers between the two numbers.

def Prog10():
    print("Prog10: Create a program that ask user to input 2 numbers.")
    print("        Print all the numbers between the two numbers.")
    print()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 < num2:
        for i in range(num1 + 1, num2):
            print(i, end=" ")
    else:        
        for i in range(num2 + 1, num1):
            print(i, end=" ")

# Create a funtion menu for program selection
def menu():
    def selection(prompt): # Create a funtion that limit the selection 
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value <= 10:
                    return value
                else:
                    print('Invalid input. Please select a number in the choices.')
            except ValueError:
                print("Invalid input. Please enter valid number.")
# Create a the selection menu
    while True:
        print()
        print("Practice Program")
        print()
        print("[1] Prog01", "\t[6]  Prog06".expandtabs(tabsize=6))
        print("[2] Prog02", "\t[7]  Prog07".expandtabs(tabsize=6))
        print("[3] Prog03", "\t[8]  Prog08".expandtabs(tabsize=6))
        print("[4] Prog04", "\t[9]  Prog09".expandtabs(tabsize=6))
        print("[5] Prog05", "\t[10] Prog10".expandtabs(tabsize=6))
        print()
        print("[0]: Exit")
        print()
        choice = selection("Select an option: ")
        print()

# Create a code that open the practice program
        if choice == 1:
            Prog01()
        elif choice == 2:
            Prog02()
        elif choice == 3:
            Prog03()
        elif choice == 4:
            Prog04()
        elif choice == 5:
            Prog05()
        elif choice == 6:
            Prog06()
        elif choice == 7:
            Prog07()
        elif choice == 8:
            Prog08()
        elif choice == 9:
            Prog09()
        elif choice == 10:
            Prog10 () 
        elif choice == 0:
            print("Exiting the program. Goodbye!")
            break

menu()