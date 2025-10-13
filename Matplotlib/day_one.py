import matplotlib.pyplot as plt
import numpy as np

x_f = float(input("Masukkan nilai x awal: "))
x_l = float(input("Masukkan nilai x akhir: "))
y_f = float(input("Masukkan nilai y awal: "))
y_l = float(input("Masukkan nilai y akhir: "))

x = np.array([x_f,x_l])
y = np.array([y_f,y_l])

plt.plot(x, y)
plt.show()
