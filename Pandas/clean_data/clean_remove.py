import pandas as pd

df = pd.read_csv('ilmuwan_nan.csv')
print("INI DATA YG ASLI")
print(df.to_string())

# df_second = df.copy()
# print('\n')
# print('INI YG MAKE ARGUMENT "inplac =True":'.center(100))
# df_second.dropna(inplace=True)
# print(df_second.to_string())

print('\n')
df_thirtd = df.copy()
df_thirtd.fillna(777, inplace = True)
print(df_thirtd.to_string())

print('\n')
df_fourth = df.copy()
df_fourth.fillna({"Lahir":"10-12-1815"}, inplace=True)
df_fourth.fillna({'Tahun Wafat':"1852"}, inplace=True)
df_fourth.fillna({'Bidang': 'Fisika'}, inplace=True)
df_fourth.fillna({'Penghargaan': "PRS"}, inplace=True)
df_fourth.fillna({'Penghargaan': "Bpk Fisika Modern"}, inplace=True)
print(df_fourth.to_string())


