"""
This script allows plotting the surface of the bed. 
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

single = True

# With reset of probe
before = [{
    "Y": 0.0,
    "X": 0.065,
    "Z": -0.0020124999999999991
}, {
    "Y": 0.0325,
    "X": 0.05629,
    "Z": -0.0014000000000000004
}, {
    "Y": 0.05629,
    "X": 0.0325,
    "Z": -0.00064999999999999943
}, {
    "Y": 0.065,
    "X": 0.0,
    "Z": 0.00011250000000000027
}, {
    "Y": 0.05629,
    "X": -0.0325,
    "Z": 0.00055000000000000025
}, {
    "Y": 0.0325,
    "X": -0.05629,
    "Z": 0.00076250000000000016
}, {
    "Y": 0.0,
    "X": -0.065,
    "Z": 0.00064999999999999986
}, {
    "Y": -0.0325,
    "X": -0.05629,
    "Z": 0.0003875000000000002
}, {
    "Y": -0.05629,
    "X": -0.0325,
    "Z": -0.00021250000000000037
}, {
    "Y": -0.065,
    "X": -0.0,
    "Z": -0.00089999999999999943
}, {
    "Y": -0.05629,
    "X": 0.0325,
    "Z": -0.0017875000000000005
}, {
    "Y": -0.0325,
    "X": 0.05629,
    "Z": -0.0022625000000000002
}, {
    "Y": 0.0,
    "X": 0.04333,
    "Z": -0.0015125000000000002
}, {
    "Y": 0.021670000000000002,
    "X": 0.03753,
    "Z": -0.0011124999999999998
}, {
    "Y": 0.03753,
    "X": 0.021670000000000002,
    "Z": -0.00062500000000000001
}, {
    "Y": 0.04333,
    "X": 0.0,
    "Z": -0.00010000000000000053
}, {
    "Y": 0.03753,
    "X": -0.021670000000000002,
    "Z": 0.00022499999999999964
}, {
    "Y": 0.021670000000000002,
    "X": -0.03753,
    "Z": 0.0003500000000000001
}, {
    "Y": 0.0,
    "X": -0.04333,
    "Z": 0.00022499999999999964
}, {
    "Y": -0.021670000000000002,
    "X": -0.03753,
    "Z": -6.2500000000000001e-05
}, {
    "Y": -0.03753,
    "X": -0.021670000000000002,
    "Z": -0.00056249999999999996
}, {
    "Y": -0.04333,
    "X": -0.0,
    "Z": -0.0010124999999999993
}, {
    "Y": -0.03753,
    "X": 0.021670000000000002,
    "Z": -0.0014500000000000001
}, {
    "Y": -0.021670000000000002,
    "X": 0.03753,
    "Z": -0.0016875
}, {
    "Y": 0.0,
    "X": 0.021670000000000002,
    "Z": -0.0010625000000000001
}, {
    "Y": 0.01083,
    "X": 0.018760000000000002,
    "Z": -0.00087500000000000002
}, {
    "Y": 0.018760000000000002,
    "X": 0.01083,
    "Z": -0.00062500000000000001
}, {
    "Y": 0.021670000000000002,
    "X": 0.0,
    "Z": -0.00037500000000000001
}, {
    "Y": 0.018760000000000002,
    "X": -0.01083,
    "Z": -0.0001875
}, {
    "Y": 0.01083,
    "X": -0.018760000000000002,
    "Z": -0.00013749999999999928
}, {
    "Y": 0.0,
    "X": -0.021670000000000002,
    "Z": -0.0001875
}, {
    "Y": -0.01083,
    "X": -0.018760000000000002,
    "Z": -0.0003875000000000002
}, {
    "Y": -0.018760000000000002,
    "X": -0.01083,
    "Z": -0.00062500000000000001
}, {
    "Y": -0.021670000000000002,
    "X": -0.0,
    "Z": -0.00085000000000000049
}, {
    "Y": -0.018760000000000002,
    "X": 0.01083,
    "Z": -0.0010499999999999997
}, {
    "Y": -0.01083,
    "X": 0.018760000000000002,
    "Z": -0.0011249999999999999
}, {
    "Y": 0.0,
    "X": 0.0,
    "Z": -0.00059999999999999962
}]
after = [{
    "Y": 0.0,
    "X": 0.072,
    "Z": 0.0
}, {
    "Y": 0.06848,
    "X": 0.02225,
    "Z": 0.00062500000000000001
}, {
    "Y": 0.04232,
    "X": -0.05825,
    "Z": 0.0017000000000000001
}, {
    "Y": -0.04232,
    "X": -0.05825,
    "Z": 0.0024625000000000003
}, {
    "Y": -0.06848,
    "X": 0.02225,
    "Z": 0.0014125000000000001
}, {
    "Y": 0.0,
    "X": 0.048,
    "Z": 0.00041250000000000011
}, {
    "Y": 0.045649999999999996,
    "X": 0.01483,
    "Z": 0.00090000000000000041
}, {
    "Y": 0.028210000000000002,
    "X": -0.038829999999999996,
    "Z": 0.0017500000000000003
}, {
    "Y": -0.028210000000000002,
    "X": -0.038829999999999996,
    "Z": 0.0021000000000000003
}, {
    "Y": -0.045649999999999996,
    "X": 0.01483,
    "Z": 0.0014125000000000001
}, {
    "Y": 0.0,
    "X": 0.024,
    "Z": 0.00098750000000000031
}, {
    "Y": 0.02283,
    "X": 0.0074199999999999995,
    "Z": 0.0012250000000000002
}, {
    "Y": 0.01411,
    "X": -0.019420000000000003,
    "Z": 0.0017125
}, {
    "Y": -0.01411,
    "X": -0.019420000000000003,
    "Z": 0.0018250000000000002
}, {
    "Y": -0.02283,
    "X": 0.0074199999999999995,
    "Z": 0.0014500000000000001
}, {
    "Y": 0.0,
    "X": 0.0,
    "Z": 0.0015000000000000002
}]

mat = np.array([[1., 0., 0.0193759 / 2], [0., 1., -0.00773554 / 2],
                [-0.01900754 / 2, 0.00779585 / 2, 1.]])

mat = ([[9.99622303e-01, 1.82391137e-04,
         -1.96197371e-02], [1.77231385e-04, 9.99914414e-01, 9.20640478e-03],
        [1.92419604e-02, -9.29200211e-03, 9.99536717e-01]])

mat = np.array([[1., 0., 0.020978 / 2], [0., 1., -0.00924437 / 2],
                [-0.02054686 / 2, 0.00933064 / 2, 1.]])

x1, y1, z1 = map(
    list,
    zip(*map(lambda d: tuple(np.array([d['X'] * 1000, d['Y'] * 1000, d['Z'] * 1000])), before)))
#x2, y2, z2 = map(list, zip(*map(lambda d: (d['X']*1000, d['Y']*1000, d['Z']*1000) , after )))

x2, y2, z2 = map(
    list,
    zip(*map(
        lambda d: tuple(np.array([d['X'] * 1000, d['Y'] * 1000, 0 * 1000]).dot(np.linalg.inv(mat))),
        before)))

fig = plt.figure()
if single:
  ax = fig.add_subplot(111, projection='3d')
else:
  ax = fig.add_subplot(211, projection='3d')

(x, y, z) = (x1, y1, z1)
# Set up the canonical least squares form
degree = 2
Ax = np.vander(x, degree)
Ay = np.vander(y, degree)
A = np.hstack((Ax, Ay))

A = np.column_stack((np.ones(len(x)), x, y))

# Solve for a least squares estimate
(coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, z)

X = np.linspace(min(x), max(x), 3)
Y = np.linspace(min(y), max(y), 3)
X, Y = np.meshgrid(X, Y)

Z = coeffs[0] + coeffs[1] * X + coeffs[2] * Y

ax.plot(x1, y1, z1, linestyle="none", marker="o", mfc="none", markeredgecolor="red")
if single:
  ax.plot(x2, y2, z2, linestyle="none", marker="o", mfc="none", markeredgecolor="green")
ax.plot_surface(X, Y, Z)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

if not single:

  ax = fig.add_subplot(212, projection='3d')
  (x, y, z) = (x2, y2, z2)
  # Set up the canonical least squares form
  degree = 2
  Ax = np.vander(x, degree)
  Ay = np.vander(y, degree)
  A = np.hstack((Ax, Ay))

  A = np.column_stack((np.ones(len(x)), x, y))

  # Solve for a least squares estimate
  (coeffs, residuals, rank, sing_vals) = np.linalg.lstsq(A, z)

  X = np.linspace(min(x), max(x), 3)
  Y = np.linspace(min(y), max(y), 3)
  X, Y = np.meshgrid(X, Y)

  Z = coeffs[0] + coeffs[1] * X + coeffs[2] * Y

  ax.plot_surface(X, Y, Z)

  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

print "Before delta: " + str(max(z1) - min(z1))
print "After  delta: " + str(max(z2) - min(z2))

plt.show()
