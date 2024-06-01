class Node:
    def __init__(self, data):
        self.data= data
        self.next= None


class LinkedList:
    def __init__(self):
        self.head= None

    def findLength(self):
        length= 0
        current= self.head

        while current:
            length= length+1
            current= current.next

        return length
    
    # function to add new node at the front of the list
    def push(self, newdata):

        newNode= Node(newdata)
        # make next of the new node as head
        newNode.next= self.head
        # move the head to point to the new node
        self.head= newNode

    #insertion at the end
    def append(self, newdata):
        newNode= Node(newdata)
        newNode.next= None

        # if the linked list is empty, make the new node as head
        if self.head is None:
            self.head= newNode
            return
        
        last= self.head
        while(last.next):
            last= last.next

        last.next= newNode
    
def traverse_link_list(head):
    # start from the head of the linked list
    current= head
    while current is not None:
        print(current.data)

        current= current.next


# head= Node(22)
# second= Node(33)
# third= Node(44)

# head.next= second
# second.next= third

# traverse_link_list(head)

ll1= LinkedList()
ll1.push(1)
ll1.push(34)
ll1.push(77)
ll1.append(121)

print(ll1.findLength())
# print(ll1)
