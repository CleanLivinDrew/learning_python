import math

def area(radius):
    a = math.pi * radius**2
    return a
res = area(3)
print(res)


def test_funct(x,y):
    if x > y:
        return(1)
    elif x < y:
        return(-1)
    elif x == y:
        return(0)

abc = test_funct(2,2)
print(abc)

