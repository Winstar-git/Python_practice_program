# Prog02: Create a program that ask user to input 2 numbers.
# Print "Equal" when the numbers are the same.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print(f"{num1} and {num2} are Equal")
else:
    print(f"{num1} and {num2} are Not Equal")
