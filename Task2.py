def getSum(number1, number2, number3):
  return number1 + number2 + number3


print('Enter 3 numbers:')
try:
  number1 = int(input()) 
  number2 = int(input()) 
  number3 = int(input()) 
except:
  print('Numbers have to be entered!')
  exit()

sum = getSum(number1, number2, number3)
print('The sum is: ' + str(sum))