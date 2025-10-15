from matplotlib import pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,8,12,23,35,67,10,110,90,150])
size = np.array([20,30,40,50,60,70,80,90,100,110])
plt.scatter(x,y, c="Black", marker="o", s=size)

x_2 = np.array([1,2,3,4,5,6,7,8,9,10])
y_2 = np.array([2,4,6,8,10,12,14,16,18,20])
size_2 = np.array([10,20,300,40,50,600,70,800,90,100])

# color = np.array(["red","blue","green","yellow","pink","orange","purple","grey","brown","cyan"]) <-- ini yg manual
# plt.scatter(x_2,y_2, s=size, c=color)  

color = np.array([10,20,30,40,50,60,70,80,90,100]) # <-- ini yg otomatis
plt.scatter(x_2,y_2, c=color, cmap='winter', s=size_2, alpha=0.5) # <--    cmap -> color map, alpha -> transparansi

plt.colorbar() # color bar buat ngasih tau skala warna

plt.show()
