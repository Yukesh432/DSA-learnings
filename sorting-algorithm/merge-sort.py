import numpy as np
import random

list1= np.random.randint(1,10, 7)
list2= np.random.randint(1,10, 7)
result= []

if len(list1)== 0:
    print(list2)
if len(list2)== 0:
    print(list1)
index_left, index_right= 0

while len(result)< len(list1)+len(list2):
    if list1[index_left]< list2[index_right]:
        result.append(list1[index_left])
        index_left+=1
    else:
        result.append(list2[index_right])
        index_right+=1
        


