import numpy as np
X = np.arange(1, 11)
print(X)

#You can use functions to generate other sequences:

Y = np.log(X)
print(Y)

Z = np.sin(X)
print(Z)

X2 = np.rad2deg(X)
print(X2 % 360)
