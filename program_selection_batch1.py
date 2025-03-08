#Insert all the programs in each fuction
 
# Prog01: Create a program that ask user to input 2 numbers.
# Print the bigger number.

def Prog01():
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

def Prog02():
    print("Prog02: Create a program that ask user to input 2 numbers.")
    print("        Print 'Equal' when the numbers are the same.")
    print()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 == num2:
        print(f"{num1} and {num2} are Equal")
    else:
        print(f"{num1} and {num2} are Not Equal")

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