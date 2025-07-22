class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return True if self.head == None else False
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
    def pop(self):
        if self.head == None:
            return "[ERROR] Stack Underflow!"
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            data = temp.data
            del temp
            return data
        
str = input()
st = Stack()

balanced = True

for c in str:
    if c == "(":
        st.push(c)
    else:
        if st.isEmpty() == False:
            st.pop()
        else:
            balanced = False
            break

if balanced == False:
    print("NO")
else:
    if st.isEmpty() == True:
        print("YES")
    else:
        print("NO")