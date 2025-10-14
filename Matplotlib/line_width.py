import matplotlib.pyplot as plt
import numpy as np

y = np.array([1,4,6,7,9,5,4,7])
x = np.array([1,2,3,4,5,6,7,8])
y_2 = np.array([2,5,7,8,10,6,5,8])
x_2 = np.array([1,2,3,4,5,6,7,8])

plt.plot(y, x, y_2, x_2, linewidth=5)
plt.show()