import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def deriv_sigmoid(x):
    return sigmoid(x) * (1-sigmoid(x))

x_train = np.array([[1,0],[0,1],[0,0],[1,1]])
y_train = np.array([[1],[1],[0],[0]])
m,n = x_train.shape

w1 = np.random.randn(x_train.shape[1], y_train.shape[1])
b1 = np.zeros((1,y_train.shape[1]))

def forward_prop(x,w,b):
    z = np.dot(x,w) + b
    gz = np.vectorize(sigmoid)
    a = gz(z)
    return z,a

def back_prop(z,a,x,y):
    dl = a - y
    deriv_sig_vec = np.vectorize(deriv_sigmoid)
    gz = deriv_sig_vec(z)
    dw = np.dot(x.T, dl*gz)/m
    db = np.sum(dl, axis=0, keepdims=True)/m
    return dw,db

for i in range(0, 1000):
    z,a = forward_prop(x_train, w1, b1)
    dw, db = back_prop(z, a, x_train, y_train)
    w1 = w1 - (.01 * dw)
    b1 = b1 - (.01 * db)

z,a = forward_prop(x_train, w1, b1)
print(a)
