class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next

        self.size += 1
    
    def search(self, key):
        i = self.head

        while i != None:
            if i.data == key:
                return i
            i = i.next
        
        return None
    
    def remove(self, data):
        loc = self.search(data)

        if loc != None:
            self.size -= 1

            if loc == self.head:
                if self.head == self.tail:
                    temp = self.head
                    self.head = None
                    self.tail = None
                    del temp
                else:
                    temp = self.head 
                    self.head = self.head.next
                    self.head.prev = None
                    temp.next = None
                    del temp
            elif loc == self.tail:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
                del temp
            else:
                loc.prev.next = loc.next
                loc.next.prev = loc.prev
                loc.prev = loc.next = None
                del loc
               


    def print_list(self):
        print("Linked List: ")
        i = self.head
        while i != None:
            print(i.data, end = " ")
            i = i.next
        print()
    
    def print_list_reverse(self):
        print("Reversed Linked List: ")
        i = self.tail
        while i != None:
            print(i.data, end = " ")
            i = i.prev
        print()

linked_list = DoublyLinkedList()

while True:
    choice = input("Do you want to add a new item to the linked list? (Y/N): ")
    if choice in ["Y", 'y']:
        data = int(input("Enter the number: "))
        linked_list.add(data)
    else:
        break

linked_list.print_list()
linked_list.print_list_reverse()

