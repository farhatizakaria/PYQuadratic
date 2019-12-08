from pack import graph
from math import sqrt

def delta_function(a,b,c):

    delta_value = (b**2) - (4*a*c)
    if delta_value < 0:
        print("There no solution for you in R")
        str(input("press any key to exit"))
        exit()
        

    elif delta_value == 0:
        x = -b / (2*a)
        print(x)

        graph.plotting(a,b,c)

    else: # which's delta_value > 0
        x1 = (- b + sqrt(delta_value)) / (2*a)
        x2 = (- b - sqrt(delta_value)) / (2*a)
        print(x1, x2)

        graph.plotting(a,b,c)
