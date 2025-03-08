#Insert all the programs in each fuction

# Prog01: Create a program that ask user to input 2 numbers.
# Print the smaller number.

def find_smaller_number():
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

def check_inequality(): 
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

def difference_of_two():
    print("Prog03: Create a program that ask user to input 2 numbers.")
    print("        Print the difference of the two numbers.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The difference of {num1} and {num2} is {num1 - num2}")

# Prog04: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers without decimal point.

def quotient_without_decimal():
    print("Prog04: Create a program that ask user to input 2 numbers.")
    print("        Print the quotient of the two numbers without decimal point.")
    print()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"The quotient of the two numbers is: {num1/num2:.0f}" )

# Prog05: Create a program that ask user to input 2 numbers. 
# Print the remainder of the two first number is divided by second number

def find_remainder():
    print("Prog05: Create a program that ask user to input 2 numbers.")
    print("        Print the remainder of the two first number is divided by second number")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The remainder of the two numbers is {num1%num2}")   

# Prog06: Create a program that ask user to input 10 numbers. 
# Printthe result of the first number minus all of the remaining numbers.

def first_subtract_all():
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

def count_even_number():
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

def print_odd_numbers():
    print("Prog08: Create a program that print all the ")
    print("        odd numbers starting from 0 to 100. (Use while loop)")
    print()
    num = 1
    while num <= 100:
        print(num, end=" ")
        num += 2

#Prog09: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero or ending five.

def skip_numbers_ending_in0and5():
    print("Prog09: Create a program that print all the numbers starting from") 
    print("        0 to 100 except numbers ending in zero or ending five.")
    print()
    for i in range(0,101):
        if i % 5 != 0:
            print(i, end=" ")
    print()

# Prog10: Create a program that ask user to input 2 numbers. 
# Print all the numbers between the two numbers.

def print_between_two_inputs():
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
        print("[1] Find the Smaller Number", "\t[6]  Subtract Multiple Numbers".expandtabs(tabsize=6))
        print("[2] Check for Inequality", "\t[7]  Count Even Numbers".expandtabs(tabsize=9))
        print("[3] Calculate the Difference", "\t[8]  Print Odd Numbers ".expandtabs(tabsize=5))
        print("[4] Quotient without Decimal", "\t[9]  Skip Numbers Ending in 0 and 5".expandtabs(tabsize=5))
        print("[5] Find the Remainder", "\t[10] Print Numbers Between Two Inputs".expandtabs(tabsize=11))
        print()
        print("[0]: Exit")
        print()
        choice = selection("Select an option: ")
        print()

# Create a code that open the practice program
        if choice == 1:
            find_smaller_number()
        elif choice == 2:
            check_inequality()
        elif choice == 3:
            difference_of_two()
        elif choice == 4:
            quotient_without_decimal()
        elif choice == 5:
            find_remainder()
        elif choice == 6:
            first_subtract_all()
        elif choice == 7:
            count_even_number()
        elif choice == 8:
            print_odd_numbers()
        elif choice == 9:
            skip_numbers_ending_in0and5()
        elif choice == 10:
            print_between_two_inputs () 
        elif choice == 0:
            print("Exiting the program. Goodbye!")
            break

menu()