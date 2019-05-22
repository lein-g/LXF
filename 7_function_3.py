import math

def quadratic(a, b, c):
    ds=(a,b,c)
    for d in ds:
        if not isinstance(d,(int,float)):
            raise TypeError('bad operand type')
    x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    y=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    return x,y