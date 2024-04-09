import numpy as np
import random

list1= np.random.randint(1,10, 7)
list2= np.random.randint(1,10, 7)
# result= []

# if len(list1)== 0:
#     print(list2)
# if len(list2)== 0:
#     print(list1)
# index_left, index_right= 0

# while len(result)< len(list1)+len(list2):
#     if list1[index_left]< list2[index_right]:
#         result.append(list1[index_left])
#         index_left+=1
#     else:
#         result.append(list2[index_right])
#         index_right+=1

# if index_right== len(list2):
#     result= result+ list1[index_left:]
#     break
n=5
for i in range(n):
    for j in range(n-i):
        print(j)
    print("\n")

