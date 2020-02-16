import scipy.integrate as integrate
from numpy import sqrt, sin, cos, pi

def func(x):
    return -sin(x)/x

I = integrate.quad(func,0,1e12)
print(I)
