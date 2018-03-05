import numpy as np
import matplotlib.pyplot as plt
import math

def my_formula1(x):
    return math.log(x, 10)

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()

xvals = np.arange(1,100, 1)
listy = [10,20,30,40,50,60,70]

print(xvals)



vec_function = np.vectorize(my_formula1)

yvals = vec_function(xvals)

print (yvals)