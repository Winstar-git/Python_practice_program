#Insert all the programs in each fuction
 
# Prog01: Create a program that ask user to input 2 numbers.
# Print the bigger number.

def compare_two_numbers():
    print("Prog01: Create a program that ask user to input 2 numbers.")
    print("        Print the bigger number.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num1 > num2:
        print(f"{num1} is bigger number.")
    else:
        print(f"{num2} is bigger number.")

# Prog02: Create a program that ask user to input 2 numbers.
# Print "Equal" when the numbers are the same.

def check_equality():
    print("Prog02: Create a program that ask user to input 2 numbers.")
    print("        Print 'Equal' when the numbers are the same.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 == num2:
        print(f"{num1} and {num2} are Equal")
    else:
        print(f"{num1} and {num2} are Not Equal")

# Prog03: Create a program that ask user to input 2 numbers.
# Print the sum of the two numbers.

def sum_of_two():
    print("Prog03: Create a program that ask user to input 2 numbers.")
    print("        Print the sum of the two numbers.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The sum of {num1} and {num2} is {num1 + num2}")

# Prog04: Create a program that ask user to input 2 numbers. 
# Print the product of the two numbers.

def product_of_two():
    print("Prog04: Create a program that ask user to input 2 numbers.")
    print("        Print the product of the two numbers.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("The product of the two numbers is: ", num1*num2) 

# Prog05: Create a program that ask user to input 2 numbers. 
# Print the quotient of the two numbers with the decimal point

def quotient_with_decimal():
    print("Prog05: Create a program that ask user to input 2 numbers.")
    print("        Print the quotient of the two numbers with the decimal point")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The quotient of the two numbers is {num1/num2:.2f}")   

# Prog06: Create a program that ask user to input 2 numbers. 
# Print the result when the first number is raised to the second number.

def exponentiation():
    print("Prog06: Create a program that ask user to input 2 numbers. Print the  ")
    print("        result when the first number is raised to the second number.")
    print()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(f"{num1} raised to the power of {num2} is {num1**num2}")

# Prog07: Create a program that ask user to input 10 numbers. 
# Print the sum of all the numbers.

def sum_of_all_numbers():
    print("Prog07: Create a program that ask user to input 10 numbers. ")
    print("        Print the sum of all the numbers.")
    print()
    sum = 0 
    for i in range(10):
        num = float(input(f"{i+1}. Enter a number: "))
        sum += num
    print(f"The sum of all the numbers is: {sum}")

# Prog08: Create a program that ask user to input 10 numbers. 
# Print how many are odd numbers.

def count_odd_numbers():
    print("Prog08: Create a program that ask user to input 10 numbers. ")
    print("        Print how many are odd numbers.")
    print()
    count = 0 
    for i in range(10):
        num = int(input(f"{i+1}. Enter a number: "))
        if num % 2 != 0:
            count += 1
    print(f"There are {count} odd numbers.")

# Prog09: Create a program that print all 
# the even numbers starting from 0 to 100. (Use for loop)

def print_even_number():
    print("Prog09: Create a program that print all the even ")
    print("        numbers starting from 0 to 100. (Use for loop)")
    print()
    for i in range(0, 101, 2):
        print(i, end=" ")

# Prog10: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero.

def skip_numbers_ending_zero():
    print("Prog10: Create a program that print all the numbers starting")
    print("        from 0 to 100 except numbers ending in zero.")
    print()
    for i in range(1, 101):
        if i % 10 != 0:
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
        print("[1] Compare Two Numbers", "\t[6]  Exponentiation".expandtabs(tabsize=6))
        print("[2] Check Equality", "\t[7]  Sum of Ten Numbers".expandtabs(tabsize=11))
        print("[3] Sum of Two Numbers", "\t[8]  Count Odd Numbers".expandtabs(tabsize=7))
        print("[4] Product of Two Numbers", "\t[9]  Print Even Numbers".expandtabs(tabsize=3))
        print("[5] Quotient with Decimal", "\t[10] Skip ending of 0".expandtabs(tabsize=4))
        print()
        print("[0]: Exit")
        print()
        choice = selection("Select an option: ")
        print()

# Create a code that open the practice program

        if choice == 1:
            compare_two_numbers()
        elif choice == 2:
            check_equality()
        elif choice == 3:
            sum_of_two()
        elif choice == 4:
            product_of_two()
        elif choice == 5:
            quotient_with_decimal()
        elif choice == 6:
            exponentiation()
        elif choice == 7:
            sum_of_all_numbers()
        elif choice == 8:
            count_odd_numbers()
        elif choice == 9:
            print_even_number()
        elif choice == 10:
            skip_numbers_ending_zero () 
        elif choice == 0:
            print("Exiting the program. Goodbye!")
            break

menu()