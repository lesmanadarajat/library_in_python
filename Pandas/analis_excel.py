import pandas as pd

read_file = pd.read_excel('orang_terkaya_2025.xlsx')


print("INI YANG VERSI HEAD".center(100), "\n")
print(read_file.head())


print("\n\n", "INI YANG VERSI TAIL".center(100), "\n")
print(read_file.tail())

print("\n\n", "INI YANG VERSI FULL".center(100))
print(read_file)

