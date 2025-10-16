import matplotlib.pyplot as plt
import numpy as np

x = np.array([40,10,50,12,8,11])
label = np.array(['merah','biru', 'hitam', 'kuning', 'hijau', 'ungu'])
meledak = (0,0.3,0,0,0,0) # meledakkan/memisahkan irisan ke 2 (biru)
color = ['red', 'blue', 'gray', 'yellow', 'green', 'purple']

plt.pie(x,labels=label, startangle=180, explode=meledak, colors=color, shadow=True)
plt.title("Data Penjualan Mobil")
plt.legend(title="car's:")
plt.show()