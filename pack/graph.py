import numpy as np
import matplotlib.pyplot as plt


def plotting(a,b,c):
    # First let's see the domin of that function
    print('1 - N')
    print('2 - R')
    domain = int(input("So which domain you have? "))
    if domain == "N" or "n":
        x = np.linspace(0,50,30)
        f = a*x**2 + b*x + c
        plt.plot(x,f)
        plt.show()

    elif domain == "R" or "r":
        x = np.linspace(-50,50,30)
        f = a*x**2 + b*x + c
        plt.plot(x,f)
        plt.show()


    else:
        print("Maybe your domain not aviable now !")
        str(input("press any key to exit"))
