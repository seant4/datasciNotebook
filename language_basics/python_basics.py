### Designed to provide basic functions of python for data science
## Pandas: Best data manipulation library
import pandas as pd

# Import data from csv
data = pd.read_csv("path/to/csv/")

# Import form excel
data = pd.read_excel("path/to/xlsx")

# Create your own data frame
data = {'A': [1,2,3], 'B': [1,2,3]}
df = pd.DataFrame(data)

# View data
df.head() # First few rows
df.tail() # Last few
df.info() # basic info
df.describe() # summary statistics

## Selecting data

# By columns
df["column"]
df["column1", "column2"]

# By row
df.loc[0] #First row
df.loc[0:2] #First three rows
df.loc[: , 'A'] #All rows for column A
df.loc[0:2, 'A'] #First 3 rows for column A

## Iteration
for index, row in df.iterrows():

##Drop data
# Drop column
df.drop(['A','B'], axis=1)
# Drop row
df.drop([0,1])

## Numpy: best numerical libraryu
import numpy as np

# Arrays:
a = np.array([1,2,3],
             [4,5,6])
a.shape() #(2,3) row x column

# Initialize array:
np.zeros(2) #[0,0]
np.ones(2) #[1,1]
np.empty(2) #[random, random]
np.arange(4) #[0,1,2,3]
np.arange(2,9,2) #[2,4,6,8])

# Manipulate array
np.sort(arr) # Sort array
np.concatenate(a,b) #Concatenate 2 arrays

## Linear algebra
np.dot(a,b) # Dot product
a @ b #preffered when a and b are 2 dimensional
np.vdot(a,b) # Vector dot product

# Lambda function
## Small anonymous function
x = lambda a : a + 10
print(x(5))

# List Comprehensions
x = [1,2,3,4,5]
x = [i + 1 for i in x]

# Merging
x = pd.DataFrame({'id' : [1,2,10,12], 'val1':['a','b','c','d']})
y = pd.DataFrame({'id' : [1,2,9,8], 'val1':['p','q','r','s']})
## Inner join
df = pd.merge(x,y,on='id', how='inner')
"""
  id val1_x val1_y
0 1  a      p
1 2  b      q
"""

## Right Outer
df = pd.merge(x,y,on='id', how='right')
"""
  id val1_x val1_y
0 1  a      p
1 2  b      q
2 9  NaN    r
3 8  NaN    d
"""

## Left outer
df = pd.merge(x,y, on='id', how='left')
"""
  id val1_x val1_y
0 1  a      p
1 2  b      q
2 10 c      NaN
3 12 d      NaN

"""

## Full outer
df = pd.merge(x,y,on='id', how='outer')
"""
  id val1_x val1_y
0 1  a      p
1 2  b      q
2 10 c      NaN
3 12 d      NaN
4 9  NaN    r
5 8  NaN    s
"""

## Full inner
df = pd.merge(x,y, left_index=True, right_index=True)
"""
  id_x va1_x id_y val1_y
0 1    a     1    p
1 2    b     2    q
2 10   c     9    r
3 12   d     8    s
"""
