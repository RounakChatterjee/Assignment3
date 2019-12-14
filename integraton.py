'''
This Program does Numerical integration using packages in Numpy and Scipy
'''
from numpy import *
from scipy.integrate import *
x = linspace(0,1,200)# Seperated data points
y = exp(x)# the function evaluated for various values of x
value_trap = trapz(y,x)#Calculates integral via trapezoidal method
value_simps = simps(y,x)#Calculates integral via simpson's method
value_romb = romberg(exp,0,1.0)#Calculates integral via Romberg method
value_gauss = fixed_quad(exp,0,1.0,n = 5)#Calculates integral via Gauss 5th order method
print("Value using trapezoidal = ",value_trap)
print("Value using simpson's= ",value_simps)
print("Value using romberg= ",value_romb)
print("Value using Gauss 5th order= ",value_gauss)