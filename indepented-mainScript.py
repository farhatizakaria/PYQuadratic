from math import sqrt # The square root
def eQuad(a,b,c):
    assert(a!=0), ("The A's value should be diffrenet to zero")
    assert(type(a) == type(b) == type(c) == int or type(a) == type(b) == type(c) == float), ("make sure about the type of the values")
    # Let's create a DELTA VALUE
    

    DELTA = (b**2) - (4*a*c)
    if DELTA == 0:
        x0 = - b / (2*a)
        return x0
    elif DELTA > 0:
        x1 = (- b + sqrt(DELTA)) / (2*a)
        x2 = (- b - sqrt(DELTA)) / (2*a)
        if x1 > x2:
            return x1, x2
        else:
            return x2,x1
    elif DELTA < 0:
        return None
