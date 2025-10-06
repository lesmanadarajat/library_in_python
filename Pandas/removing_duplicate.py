import pandas as pd

health = pd.read_csv('health_data.csv')
# print(health.to_string())

print(health.duplicated())

health.drop_duplicates(inplace = True)

print(health.to_string())
print(health.duplicated())