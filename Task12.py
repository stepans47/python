import math

class NotQuadraticException(Exception):
    pass

def isEquationQuadratic(coefA):
    return coefA != 0

def getDiscriminant(a, b, c):
    d = b**2-4*a*c
    return d

def getNumberOfRoots(discriminant):
    if(discriminant < 0):
        return 0
    elif(discriminant == 0):
        return 1
    else:
        return 2

def getQuadraticEquationRoots(a, b, c):
    discriminant = getDiscriminant(a, b, c)
    discriminantSquareRoot = math.sqrt(abs(discriminant))

    rootsNumber = getNumberOfRoots(discriminant)
    if(rootsNumber == 0):
        return None
    elif(rootsNumber == 1):
        x = (-b + discriminantSquareRoot) / 2 * a
        return [x]
    else:
        x1 = (-b + discriminantSquareRoot) / 2 * a
        x2 = (-b - discriminantSquareRoot) / 2 * a
        return [x1, x2]


print('Enter 3 coefficients for quadratic equation (a, b, c):')
try:
   a = int(input()) 
   if not (isEquationQuadratic(a)):
       raise NotQuadraticException("Equation is not quadratic")

   b = int(input()) 
   c = int(input()) 
except NotQuadraticException as ex:
   print(ex)
   exit()
except Exception as ex:
   print('Numbers have to be entered!')
   exit()

result = getQuadraticEquationRoots(a, b, c)
if(result == None):
    print("Equation has no solutions")
elif(len(result) == 1):
    print("Equation has following solution: " + str(result[0]))
else:
    print("Equation has following solutions: " + str(result[0]) + " and " + str(result[1]))