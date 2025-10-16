import matplotlib.pyplot as plt
import numpy as np

sumbu_x = np.random.normal(177,10,1000) # (mean, std, jumlah data)
plt.hist(sumbu_x)
plt.show()