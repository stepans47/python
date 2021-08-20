print("Enter 2 numbers for mathematical operations (operand 1 and operand 2):")
try:
    number1 = int(input())
    number2 = int(input())
except:
    print("You have to input numbers!")
    exit()

addition = number1 + number2
print(str(number1) + " + " + str(number2) + " = " + str(addition))

subtraction = number1 - number2
print(str(number1) + " - " + str(number2) + " = " + str(subtraction))

multiplication = number1 * number2
print(str(number1) + " * " + str(number2) + " = " + str(multiplication))

if(number2 == 0):
    print("You cannot divide on zero!")
else:
    division = number1 / number2
    print(str(number1) + " / " + str(number2) + " = " + str(division))