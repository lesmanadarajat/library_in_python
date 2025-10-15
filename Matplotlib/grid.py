import matplotlib.pyplot as plt
import numpy as np

bulan = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
penjualan = np.array([1,17,14,25,5,11,6,10,7,10,2,17])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}


plt.title("Diagram Penjualan Barang", fontdict = font1)
plt.xlabel("bulan", fontdict = font2)
plt.ylabel("jumlah barang terjual", fontdict = {'family':'serif','color':'green','size':15})
plt.plot(bulan, penjualan, ls = '-.', color = 'red', linewidth = 1.5)

# di atas ^ codingan -> labels.py 


## main

# axis, untuk nampilin sumbu mana yg di kasih grid/garis

# plt.grid(axis= 'x', color = 'black', linestyle = '--', lw = 0.5)
# plt.grid(axis= 'y', color = 'black', linestyle = '--', lw = 0.5)
plt.grid(axis= 'both', color = 'black', linestyle = '--', lw = 0.5) # both -> x & y, ini juga udh default


plt.show()