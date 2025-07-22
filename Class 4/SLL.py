class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, data):
        temp = Node(data)
        self.size += 1

        if self.head == None: # list is empty
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = self.tail.next # self.tail = temp
    
    def print_list(self):
        print("Linked List: ")
        i = self.head
        while i != None:
            print(i.data, end = " ")
            i = i.next
        print()
    
    def find_middle(self):
        if self.size%2==0:
            return None
        
        second_leg = self.head
        first_leg = self.head

        while first_leg!= self.tail:
            first_leg = first_leg.next.next
            second_leg = second_leg.next

        return second_leg


linked_list = SingleLinkedList()

while True:
    choice = input("Do you want to add a new item to the linked list? (Y/N): ")
    if choice in ["Y", 'y']:
        data = int(input("Enter the number: "))
        linked_list.add(data)
    else:
        break

linked_list.print_list()
print(linked_list.find_middle().data)

