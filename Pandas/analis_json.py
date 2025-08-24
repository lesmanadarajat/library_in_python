import pandas as pd

display = pd.options.display.max_rows = 9999

read_jsn = pd.read_json('scientist.json')

print(f"ini isi dari file scientist.json\n{read_jsn}")

print('\n ini dari method head(2) ')
print(read_jsn.head(2))

print('\n ini dari method tail(2)')
print(read_jsn.tail(2))


# import json as jsn
# with open('scientist.json', mode='r', encoding='utf-8') as file:
#     read = jsn.load(file)
#     print(jsn.dumps(read, indent=4))

print(display)