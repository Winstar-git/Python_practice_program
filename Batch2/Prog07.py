# Prog07: Create a program that ask user to input 10 numbers. 
# Print how many are even numbers.

count = 0
for i in range(1,11):
    num = int(input(f"{i}. Enter a number: "))
    if num % 2 == 0:
        count += 1
print(f"There are {count} even numbers")