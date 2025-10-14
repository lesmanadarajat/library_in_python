import matplotlib.pyplot as plt
import numpy as np

y = np.array([1,4,6,7,9,5,4,7])
y_2 = np.array([2,5,7,8,10,6,5,8])
y_3 = np.array([3,6,8,9,11,7,6,9])

plt.plot(y, color='black')
plt.plot(y_2, color='#45587d', ls='-.', marker='o')
plt.plot(y_3, color='0.75', ls=':', marker='x')


plt.show()