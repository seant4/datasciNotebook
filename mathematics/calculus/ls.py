import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1],[2],[3],[4]])
y = np.array([[1],[3],[2],[4]])

# we hope to apply least squares to this
b = np.linalg.inv((x.T @ x)) * (x.T @ y)
b_num = np.zeros(4)
for i in range(0, len(x)):
   b_num[i] = b[0] * x[i][0]


plt.plot(x,b_num)
plt.scatter(x,y)
plt.show()
