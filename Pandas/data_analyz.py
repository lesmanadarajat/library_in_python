import pandas as pd 

pd.options.display.max_rows = 99999

read_data = pd.read_csv('ai_human.csv')
# print(read_data)


print('ini head\n{}'.format(read_data.head()))

print(f'ini tail\n{read_data.tail()}')

print(read_data.info())

print(pd.options.display.max_rows)

