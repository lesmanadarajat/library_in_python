import pandas as pd

df = pd.read_csv('objek_percobaan.csv')
print(df)


# #fill in the value with the mean
# mean_df = df.copy()
# x = df['Umur'].mean()
# mean_df.fillna({'Umur':x}, inplace=True)
# print(mean_df.to_string())

# #fill in the value with the median
# median_df = df.copy()
# y = df['Tinggi_Badan'].median()
# median_df.fillna({'Tinggi_Badan':y}, inplace=True)
# print(median_df.to_string())

# #fill in the value with the modus
# modus_df = df.copy()
# z = df['Berat_Badan'].mode()[0]
# modus_df.fillna({'Berat_Badan':z}, inplace=True)
# print(modus_df.to_string)


mean_median_mode_df = df.copy()
x = df['Umur'].mean()
mean_median_mode_df.fillna({'Umur':x}, inplace=True)
y = df['Tinggi_Badan'].median()
mean_median_mode_df.fillna({'Tinggi_Badan':y}, inplace=True)
z = df['Berat_Badan'].mode()[0]
mean_median_mode_df.fillna({'Berat_Badan':z}, inplace=True)
print(mean_median_mode_df.to_string)