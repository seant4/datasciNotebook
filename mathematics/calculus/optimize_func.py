import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

# Define data
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,3,2,4,3,5,4,6,5,7]
z = [1,2,3,4,5,5,4,3,2,1]

# Arrange data
x_stack = np.column_stack((x,y))
pol = PolynomialFeatures(degree=2)
x_pol = pol.fit_transform(x_stack)

# Regress
model = linear_model.LinearRegression()
model.fit(x_pol, z)
z_pred = model.predict(x_pol)

# Plotting
fig = plt.figure()
ax=fig.add_subplot(projection='3d')
ax.scatter(x,y,z, color='blue')

x_range = np.linspace(min(x), max(x), 10)
y_range = np.linspace(min(y), max(y), 10)
x_mesh, y_mesh = np.meshgrid(x_range, y_range)
x_poly_mesh = pol.transform(np.column_stack((x_mesh.flatten(), y_mesh.flatten())))
z_poly_mesh = model.predict(x_poly_mesh).reshape(x_mesh.shape)

# Gradient optimization
gradient_x = model.coef_[0] * np.ones_like(x_mesh)
gradient_y = model.coef_[1] * np.ones_like(y_mesh)

# Plot
ax.scatter(x,y,z, color='blue')
ax.plot_surface(x_mesh, y_mesh, z_poly_mesh, alpha=0.5)
ax.quiver(x_mesh, y_mesh, np.zeros_like(x_mesh), gradient_x, gradient_y, np.zeros_like(x_mesh))
plt.savefig('optimum.png')
