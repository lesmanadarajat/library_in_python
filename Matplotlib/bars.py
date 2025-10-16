import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A','B','C','D','E','F','G','H','I','J'])
y = np.array([5,7,4,6,8,7,9,12,11,10])

plt.bar(x,y, color='black', width=1.3) # bar  versi biasa 

# plt.barh(x,y, color='cyan', height=2) -> barh versi horizontal
plt.title("Bar Chart")
plt.show()

