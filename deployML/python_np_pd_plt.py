a = 3
print(a)
a = "abc"
print(a)
a = 4
b = 5
print(a+b)
print(a*b)

my_list = [10,20,30,40]
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])

my_list_2 = [10,"abd",30,40]
print(my_list_2[-3])

if 3 < 4:
    print("within if loop")
print("outside if loop")

for i in range(10):
    print(i)
    
new_list = []
for i in my_list:
    print(i)
    new_list.append(i*3)


def calculatesSum(a,b):
    return a+b

print(calculatesSum(3, 4))

def calculateSumAndDivision(a,b):
    return a+b, a/b

var1, var2 = calculateSumAndDivision(10, 2)
print(var1)
print(var2)

with open("my_fiel_1.txt", "w") as f:
    f.write("sample content 1")
    
with open("my_fiel_1.txt", "a") as f:
    f.write("more content")
    
    
import numpy as np

sample_list = [10,20,30,40,50,60]

sample_numpy_1d_array = np.array(sample_list)

sample_numpy_2d_array = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

new_arr = sample_numpy_2d_array.reshape(2,6)

new_arr2 = sample_numpy_2d_array.reshape(1,-1)
    
new_arr3 = sample_numpy_2d_array.reshape(-1,1)

new_sample = sample_numpy_2d_array[1:3,2:4]


import pandas as pd

sample_series = pd.Series([10,20,30,40])

sample_series_2 = pd.Series([10,20,30,40],['A','B','C','D'])
    
sample_series_2[2]

sample_series_2['C']

sample_dataframe = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

sample_dataframe_2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[10,11,12]],['Row1','Row2','Row3','Row4'],['Column1','Column2','Column3'])
    
sample_dataframe_2['Column3']    

sample_dataframe_2[['Column1','Column3']] 

sample_dataframe_2.loc['Row1']   
    
sample_dataframe_2.loc[['Row2','Row3'],['Column2','Column3']]   
    
sample_dataframe_2.iloc[0:2, 1:3] 

sample_dataframe_2.iloc[1:2, 2:4] 

sample_dataframe_2.iloc[:, :-1] 

type(sample_dataframe_2.iloc[:, :-1])

new_numpy_array_2 = sample_dataframe_2.iloc[:, :-1].values

sample_dataframe_2['Column1']>4

sample_dataframe_2[sample_dataframe_2['Column1']>4]

df = pd.read_csv("storepurchasedata.csv")

df.describe()
df.info()
df.head()
df.head(2)

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,25,35,40,50,60,80,90,95,100]

plt.plot(x,y)
    
plt.scatter(x,y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sample plot')
plt.plot(x,y)

plt.hist([10,20,20,30,30,30,40,40,50])

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary Analysis')
plt.plot(df['Age'], df['Salary'])













    
    
    
    
    
    
    
    
    
    
    
    