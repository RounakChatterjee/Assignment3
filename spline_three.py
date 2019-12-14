'''
This program showcases the use of Cubic spline  interpolation using 
scipy packages
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import * 
x = [0,1,2,3,4,5]
y = [1.0,2.0,1.0,0.5,4.0,8.0]# Given data
spl = InterpolatedUnivariateSpline(x, y,k=3)#univariate cubic spline
plt.xlabel("X values")
plt.ylabel("Y values")
plt.scatter(x, y,label = "Data points",color = 'red')# Plot's experimental points
xs = np.linspace(0,5, 1000)
plt.title("Cubic spline interpolation")
plt.plot(xs, spl(xs), color = (0.0,1.0,0.0))
plt.grid()
plt.show()

