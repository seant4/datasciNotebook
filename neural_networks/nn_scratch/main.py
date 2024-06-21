import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def deriv_sigmoid(x):
    return sigmoid(x) * (1-sigmoid(x))

x_train = np.array([[1,0],[0,1],[0,0],[1,1]]) # Row = sample, Column = Feature
y_train = np.array([[0,1],[0,1],[0,0],[0,0]]) #one hot encoding of our output [1,0] represents 0, [0,1] represents 1
m,n = x_train.shape

# Weights and biases
w1 = np.random.randn(4,4) # Should be based on what we want the output to be
b1 = np.random.randn(2)

# Forward Propigation
z1 = (w1.T @ x_train) + b1
# Sigmoid activation for this example
for i in range(0, len(z1)):
    for j in range(0, len(z1[i])):
        z1[i][j] = sigmoid(z1[i][j])

# Back propigation
dz1 = y_train - z1
dw1 = 1 / m * dz1.dot(z1.T)
db1 = 1 / m * np.sum(dz1)

# Update our parameters
alpha = 0.1
w1 = w1 - alpha * dw1
b1 = b1 - alpha * db1

# Prediction
z1 = (w1.T @ x_train) + b1
# Sigmoid activation for this example
for i in range(0, len(z1)):
    for j in range(0, len(z1[i])):
        z1[i][j] = sigmoid(z1[i][j])

print(z1)
