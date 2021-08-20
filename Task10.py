def sign(x):
    if(x > 0):
        return 1
    elif(x < 0):
        return -1
    else:
        return 0


isNumberIncorrect = True
while(isNumberIncorrect):
    print("Enter one number and it's sign will be received:")
    try:
        number = int(input())
        isNumberIncorrect = False
    except:
        print("You have to input a number!")
        exit()

print("Ths sign is: " + str(sign(number)))