#Prog09: Create a program that print all the numbers starting 
# from 0 to 100 except numbers ending in zero or ending five.

for i in range(0,101):
    if i % 5 != 0:
        print(i, end=" ")
print()
