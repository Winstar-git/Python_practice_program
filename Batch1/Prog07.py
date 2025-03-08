# Prog07: Create a program that ask user to input 10 numbers. 
# Print the sum of all the numbers.

sum = 0 
for i in range(10):
    num = float(input(f"{i+1}. Enter a number: "))
    sum += num
print(f"The sum of all the numbers is: {sum}")
