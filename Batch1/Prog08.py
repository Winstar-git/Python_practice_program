# Prog08: Create a program that ask user to input 10 numbers. 
# Print how many are odd numbers.

count = 0 
for i in range(10):
    num = int(input(f"{i+1}. Enter a number: "))
    if num % 2 != 0:
        count += 1
print(f"There are {count} odd numbers.")
