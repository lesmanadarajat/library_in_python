import matplotlib.pyplot as plt
import numpy as np


# plot 1
x = np.array([1,2,3,4,5])
y = np.array([10,20,25,30,40])
plt.subplot(3,3,1) # (baris, kolom, index ke brp)
plt.plot(x,y)


# plot 2
x_2 = np.array([1,2,3,4,5])
y_2 = np.array([40,30,25,20,10])
plt.subplot(3,3,2) # (baris, kolom, index ke brp)
plt.plot(x_2,y_2)


# plot 3
x_3 = np.array([1,2,3,4,5])
y_3 = np.array([1,4,9,16,25])
plt.subplot(3,3,3) # (baris, kolom, index ke brp)
plt.plot(x_3,y_3)


# plot 4
x_4 = np.array([1,2,3,4,5])
y_4 = np.array([25,16,9,4,1])
plt.subplot(3,3,4) # (baris, kolom, index ke brp)
plt.plot(x_4,y_4)


# plot 5
x_5 = np.array([1,2,3,4,5])
y_5 = np.array([5,10,15,20,25])
plt.subplot(3,3,5) # (baris, kolom, index ke brp)
plt.plot(x_5,y_5)


# plot 6
x_6 = np.array([1,2,3,4,5])
y_6 = np.array([25,20,15,10,5])
plt.subplot(3,3,6) # (baris, kolom, index ke brp)
plt.plot(x_6,y_6)

# plot 7
x_7 = np.array([1,2,3,4,5])
y_7 = np.array([2,3,5,7,11])
plt.subplot(3,3,7) # (baris, kolom, index ke brp)
plt.plot(x_7,y_7)


# plot 8
x_8 = np.array([1,2,3,4,5])
y_8 = np.array([11,7,5,3,2])
plt.subplot(3,3,8) # (baris, kolom, index ke brp)
plt.plot(x_8,y_8)


# plot 9
x_9 = np.array([1,2,3,4,5])
y_9 = np.array([3,1,4,1,5])
plt.subplot(3,3,9) # (baris, kolom, index ke brp)
plt.plot(x_9,y_9)


plt.show()