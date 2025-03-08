# Prog06: Create a program that ask user to input 10 numbers. 
# Printthe result of the first number minus all of the remaining numbers.

sum = 0
first = int(input("1. Enter a number: "))
for i in range(2,11):
    num = int(input(f"{i}. Enter a number: "))
    sum += num
r = first - sum
print(f"The result of the first number minus all of the remaining numbers: {r}")
