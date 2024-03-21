import random
import numpy as np

# creating a list of random number
list1= np.random.randint(1,10, 5)
# list2= np.random.randint(20,30, 5)
print("before sorting........\n")
print(list1)
sorted_list= []

for i in range(0, len(list1)+1):
    for item in list1:
        if list1[i]> list1[i+1]:
            pass
        else:
            temp= list1[i+1]
            list1[i]= temp
            list1[i+1]= list1[i]
    print(i)
    # if list1[i+1]>list1[i]:
    #     temp= list1[i+1]
    #     list1[i]= temp
    #     list1[i+1]= list1[i]
    #     # sorted_list.append(list1[i+1])
    # else:
    #     pass
        # sorted_list.append(list1[i])


#     if list1[index]> list1[index+1]:
#         sorted_list.append(list1[index])
#     else:
#         sorted_list.append(list1[index+1])

print("List after Bubble sort::")
print(list1)

