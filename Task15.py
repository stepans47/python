def isTriangleValid(a, b, c):
    if(a > b and a > c):
        return b + c > a
    elif(b > a and b > c):
        return a + c > b
    else:
        return a + b > c

def isTriangleEquilateral(a, b, c):
    return a == b and a == c and b == c

def isTriangleIsosceles(a, b, c):
    return (a == b and a != c) or (a == c and a != b) or (b == c and b != a)

def main():
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

    if(isTriangleEquilateral(a, b, c)):
        print("Triangle is equilateral")
    if(isTriangleIsosceles(a, b, c)):
        print("Triangle is isosceles")
    else:
        print("It's not a proper triangle")

main()