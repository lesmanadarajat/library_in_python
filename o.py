import zipfile
import pandas as pd

# Series for one dimensional
print("ini yg Series")
a = pd.Series({'A' : [1,2,5],
               'B' : [1,8,7],
               'C' : [9,5,7]})

b = {'umur' : 17,
     'nama' : "dadang"}
c  = pd.Series(b)

print(a)
print(c)


# DataFrame for two dimensional
print("\nini yg DataFrame")
x = pd.DataFrame({'X' : [1,7,8],
                  'y' : [0,9,7,],
                  'z' : [9,4,5]})

y = {'nama' : ['ujang'],
     'umur' : [19]}
z = pd.DataFrame(y)

print(x)
print(z)

