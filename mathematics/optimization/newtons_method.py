import numpy as np

def newtons_method(f, df, x0, e, N):
    xn = x0
    for i in range(0, N):
        fx = f(xn)
        if abs(fx) < e:
            return xn
        dfx = df(xn)
        if dfx == 0:
            return None
        xn = xn - fx/dfx
    return None

# Function to analyze
def sgr(x):
    return (x**3) - (x**2) - 1

def dsgr(x):
    return (3*x**2) - (2*x)

print(newtons_method(sgr, dsgr, 0.1, .0001, 100))
