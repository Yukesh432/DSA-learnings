# Traversal in a singly linked list 

class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

    
def traverse_link_list(head):

    # start from the head of the linked list
    current= head

    while current is not None:
        print(current.data)

        current= current.next

    print()


head= Node(22)
second= Node(33)
third= Node(44)

head.next= second

traverse_link_list(head)