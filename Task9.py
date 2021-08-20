print("Enter 2 numbers to find out the smaller:")
try:
    number1 = int(input())
    number2 = int(input())
except:
    print("You have to input numbers!")
    exit()

if(number1 < number2):
    print("The smaller number is: " + str(number1))
elif(number2 < number1):
    print("The smaller number is: " + str(number2))
else:
    print("Numbers are equal")