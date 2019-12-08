# calling the importants libraries
from time import sleep


# importing the modules in package folder

from pack import delta_verify as dv




def eQuation():
    #We have get 3 values
    a = float(input("Please enter the value of a "))
    if a != 0:
        b = float(input("Also the value of b "))
        c = float(input("Finally of c "))
        dv.delta_function(a,b,c)
        str(input("press any key to exit "))
        exit()
    else:
        print("a value should be different 0")




eQuation()
