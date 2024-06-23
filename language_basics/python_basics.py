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
