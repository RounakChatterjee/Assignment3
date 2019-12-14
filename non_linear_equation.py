'''
This python program solves the given non linear equation by various methods 
'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import * 
def f(x):# the function
	return np.sin(np.cos(np.exp(x)))
'''
Root finding by bisection method in the range (-1.0,1.0).
'''
root = bisect(f,-1.0,1.0)
print("root of the function sin(cos(exp(x))) = 0 is : ",root)
print("Value f(x) = ",f(root))#We an readily observe that it is not completely zero but evaluated to some toleran
'''
This function calculatesthe root the function usng newton rapson method by using the information about it's derivative.
'''
def func(x):# the derivative of the function
	return -np.exp(x)*np.cos(np.cos(np.exp(x)))*np.sin(np.exp(x))
root2= newton(f,-1.0,fprime = func)# evaluated with initial guess at x = -1.0
root3= newton(f,-0.1,fprime = func)# evaluated with initial guess at x = -0.1
root4= newton(f,-1.0)# this one find's the root using secant method

print("root with initial guess at -1.0= ",root2)
print("Value f(x) = ",f(root2))
print("root with initial guess at -0.1 = ",root3)
print("Value f(x) = ",f(root3))
print("root using secant method with initial guess at -1.0= ",root4)
print("Value f(x) = ",f(root4))


'''
The answer for each of the initial guesses changes because the newton Raphson method for different values of initial conditions, the roots might fall at different places.
'''
x = np.linspace(-2.5,10,200)
y = f(x)
l1 = func(-1.0)*x+f(-1.0)
plt.plot(x,y)
plt.plot(x,l1)
plt.grid()
plt.show()