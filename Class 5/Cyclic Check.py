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
node6.next = node3





head = node1
temp = head

visited = []
isCyclic = False

while temp != None:
    if temp in visited:
        print("Cyclic!")
        print(temp.data)
        isCyclic = True
        break
    else:
        visited.append(temp)
        temp = temp.next

if isCyclic == False:
    print("Acyclic!")

