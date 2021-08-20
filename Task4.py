import math

def getSquareSideLength(area):
  sideLength = math.sqrt(area)
  return sideLength


print("Enter square's area:")
areaInput = input()

try:
  areaParam = int(areaInput)
except:
  print('Area has to be a figure!')
  exit()

sideLenth = str(getSquareSideLength(areaParam))
print("Based on the area, length of the square's side will be: " + sideLenth)