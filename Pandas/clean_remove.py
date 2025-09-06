import pandas as pd
import keyword as ky

df = pd.read_csv('ilmuwan_nan.csv')
print("INI DATA YG ASLI")
print(df.to_string())

print('\n')
print('INI YG MAKE ARGUMENT "inplac =True":'.center(100))
df.dropna(inplace=True)
print(df.to_string())


