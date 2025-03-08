# Prog01: Create a program that ask user to input 2 numbers.
# Print the smaller number.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 < num2:
    print(f"{num1} is smaller number.")
else:
    print(f"{num2} is smaller number.")
