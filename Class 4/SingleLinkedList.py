class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class SingleLinkedList:
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
            self.tail = self.tail.next

        self.size += 1
    
    def add_first(self, data):
        if self.head is None:
            self.add(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node
        self.size += 1

    def add_after(self, key, data):
        temp = self.__search(key)

        if temp is None:
            return
        else:
            node = Node(data)
            node.next = temp.next
            temp.next = node
            self.size += 1

            if node.next is None:
                self.tail = node

    def search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return "FOUND"
            temp = temp.next
        return "NOT FOUND"
    
    def __search(self, key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return temp
            temp = temp.next
        return None

    def __str__(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
        return ""
    
    def remove(self,key):
        if self.size == 0:
            return
        elif self.size == 1 and self.head.data == key:
            node = self.head 
            self.head = None
            self.tail = None
            self.size = 0
            del node
        else:
            if self.head.data == key:
                node = self.head 
                self.head = self.head.next
                del node 
                self.size -= 1
            else:
                temp = self.head

                while temp.next is not None and temp.next.data != key:
                    temp = temp.next

                if temp.next is None:
                    return
                else:
                    node = temp.next 
                    temp.next = node.next
                    node.next = None
                    del node
                    self.size -= 1 

        
        


linkedList = SingleLinkedList()
for i in range(10, 101, 10):
    linkedList.add(i)

print(linkedList)

linkedList.add_first(110)
print(linkedList)

linkedList.add_after(30, 35)
print(linkedList)

linkedList.add_after(100, 105)
print(linkedList)