"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Creating a node

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head= None

    def append(self, data):
        new_node= Node(data)
        if not self.head:
            self.head= new_node
        else:
            current= self.head
            while current.next:
                current= current.next
            current.next= new_node

    def display(self):
        current= self.head
        while current:
            print(current.data, end= "-->")
            current= current.next
        print("None")

    
my_list= LinkedList()

#append elelments to the linked list
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.display()