import scipy.integrate as integrate
from numpy import sqrt, sin, cos, pi
import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return sin(x)/x

li = []
for t in range(int(1e-6),int(100*np.pi),int(np.pi)):
    I = integrate.quad(func,0,t)
    li.append(I[0]/np.pi)

x = np.linspace(1e-6,100*np.pi,105)
plt.plot(x, li)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
