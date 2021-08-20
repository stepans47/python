def getPreviousNumber(number):
  return number - 1

def getNextNumber(number):
  return number + 1


print('Input a number please:')
inputNumber = input()

try:
  paramNumber = int(inputNumber)
except:
  print('Number has to be entered!')
  exit()

print('Previous number: ' + str(getPreviousNumber(paramNumber)))
print('Next number: ' + str(getNextNumber(paramNumber)))