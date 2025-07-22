class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(4)
node5 = Node(6)
node6 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6



def print_list(head):

    temp = head
    while temp != None:
        print(f"{temp.data}->" if temp.next!=None else f"{temp.data}", end="")
        temp = temp.next
    print()
    
def reverse(head):
    currPrev = None
    curr = head
    currNext = head.next

    while curr != None:
        curr.next = currPrev

        currPrev = curr
        curr = currNext
        if currNext != None:
            currNext = currNext.next
    
    return currPrev

head = node1
print_list(head)

head = reverse(head)
print_list(head)