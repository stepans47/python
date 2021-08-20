def isOperationValid(operation):
    validOperations = ['+', '-', '*' ,'/']
    if(operation in validOperations):
        return True
    else:
        return False


areNumbersIncorrect = True
while(areNumbersIncorrect):
    print("Enter 2 numbers for mathematical operations (operand 1 and operand 2):")
    try:
        number1 = int(input())
        number2 = int(input())
        areNumbersIncorrect = False
    except:
        print("You have to input numbers!")

isOperationIncorrect = True
while(isOperationIncorrect):
    print("Enter operation you want to execute (+, -, *, /):")
    try:
        operation = input()
        if not(isOperationValid(operation)):
            raise Exception("Operation is invalid!")
        isOperationIncorrect = False
    except Exception as ex:
        print(ex)

result = eval(str(number1) + operation + str(number2))
print(str(number1) + ' ' + operation + ' ' + str(number2) + " = " + str(result))