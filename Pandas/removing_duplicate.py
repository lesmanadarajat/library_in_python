import pandas as pd

data = pd.read_csv('health_data.csv')
# print(data.to_string())

print(data.duplicated())

data.drop_duplicates(inplace = True)

print(data.to_string())

print(data.duplicated())
