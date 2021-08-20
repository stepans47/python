import math

def isTriangleValid(a, b, c):
    if(a > b and a > c):
        return b + c > a
    elif(b > a and b > c):
        return a + c > b
    else:
        return a + b > c

def getTrianglePerimeter(a, b, c): 
  return a + b + c

def getTriangleSemiPerimeter(a, b, c): 
  return (a + b + c)/2

def getTriangleArea(a, b, c):
  sp = getTriangleSemiPerimeter(a, b, c)
  area = math.sqrt(sp*(sp - a)*(sp - b)*(sp - c))
  return area


print("Enter triangle's sides length:")
try:
  a = int(input())
  b = int(input())
  c = int(input())
except:
  print("Triangle's sides have to be figures!")
  exit()

if not (isTriangleValid(a, b, c)):
    print("Triangle is not valid!")
    exit()

perimeter = str(getTrianglePerimeter(a, b, c))
area = str(getTriangleArea(a, b, c))

print("Triangle's perimeter is: " + perimeter)
print("Triangle's area is: " + area)