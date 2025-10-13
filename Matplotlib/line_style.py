import matplotlib.pyplot as plt
import numpy as np


# linestyle or ls
# dotted or ':'
# dashed or '--'
# solid or '-'
# dashdot or '-.'
# no line or ' '

y   = np.array([3, 6, 8, 5, 9, 7, 10])
y_2 = np.array([5, 3, 10, 7, 11, 9, 8])
y_3 = np.array([7, 10, 4, 9, 13, 11, 7])
y_4 = np.array([9, 5, 14, 7, 15, 13, 14])
y_5 = np.array([1, 14, 17, 13, 17, 15, 3])
y_6 = np.array([2, 17, 20, 16, 20, 18, 4])

plt.plot(y, ls = 'dashed', marker = 'x')
plt.plot(y_2, ls = 'dashdot', marker = 'o')
plt.plot(y_3, ls = ':', marker = '*')
plt.plot(y_4, ls = '-', marker = 's')
plt.plot(y_5, ls = ' ', marker = '^')
plt.plot(y_6, ls = 'None', marker = 'p')

plt.show()
