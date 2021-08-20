import random

print("Enter 2 numbers for range interval (start and end):")
try:
    start = int(input())
    end = int(input())
except:
    print("You have to input numbers!")
    exit()

integerNumber = random.randint(start, end)
floatNumber = random.uniform(start, end)

print("Integer random number is: " + str(integerNumber))
print("Float random number is: " + str(floatNumber))