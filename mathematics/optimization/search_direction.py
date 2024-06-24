import numpy as np
import matplotlib.pyplot as plt

def quad(x):
    return (((-1/4) * (x*x)) + x)

y = np.zeros(5)
x = np.arange(0, 5)
for i in range(0, len(x)):
    print(i)
    y[i] = quad(i)

plt.plot(x,y)
plt.show()
