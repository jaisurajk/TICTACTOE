import numpy as np
x = np.arange(0, np.pi*2, 0.1)
y = np.cos(x)+ np.sin(x)
z=x[np.argmax(y)]
print(z)