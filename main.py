class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def insertatbeggining(head,x):
    newnode=Node(x)
    newnode.next=head
    return newnode
def traverse_list(head):
    temp=head
    while temp is not None:
        print(temp.data,end="")
        if temp.next is not None:
            print("->",end="")
        temp=temp.next
    print()


if __name__=="__main__":
    node1=Node(10)
    node2=Node(20)
    node3=Node(30)
    node4=Node(40)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    head=node1
    head=insertatbeggining(head,23)
    traverse_list(head)

