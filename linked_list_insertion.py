class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        self.new_node=Node(data)
        if self.head is None:
            self.head=self.new_node
        else:
            self.new_node.next=self.head
            self.head=self.new_node
        print("\n{0} element was inserted into the linked list".format(self.new_node.data))
    def insert_end(self,data):
        self.new_node=Node(data)
        self.current=self.head
        while(self.current.next):
            self.current=self.current.next
        self.current.next=self.new_node
        print("\n{0} element was inserted at the end of linked list".format(self.new_node.data))
    def insert_pos(self,data,index):
        self.new_node=Node(data)
        self.index=index
        self.count=0
        if self.index == 0:
            insert_begin(self.new_node)
        else:
            self.current=self.head
            while(self.current.next and  self.count < self.index-1):
                self.current=self.current.next
                self.count=self.count+1
            self.new_node.next=self.current.next
            self.current.next=self.new_node
        print("\n{0} element is inserted at {1} position".format(self.new_node.data,self.index))
    def display(self):
        print("elements in the Linked List are:")
        if self.head == None:
            print("Linked list is empty")
        else:
            self.current=self.head
            while(self.current):
                print(self.current.data,end="...")
                self.current=self.current.next
    def insert(self,data):
        self.new_node=Node(data)
        if self.head is None:
            self.head=self.new_node
        else:
            self.new_node.next=self.head
            self.head=self.new_node
def choice():
    l=LinkedList()
    print()
    l.insert(60)
    l.insert(50)
    l.insert(40)
    l.insert(30)
    l.insert(20)
    l.insert(10)
    l.display()
    print("\n")
    print("1.Insert element at the BEGIN")
    print("2.Insert element at the END")
    print("3.Insert element at the SPECIFIED POSITION")
    print()
    ch=int(input("Enter your choice do u want to perform insertion:"))
    if ch == 1:
        ele=int(input("Enter element:"))
        l.insert_begin(ele)
        l.display()
    elif ch == 2:
        ele=int(input("enter element:"))
        l.insert_end(ele)
        l.display()
    elif ch == 3:
        ele=int(input("enter element:"))
        pos=int(input("enter position where do u want to insert:"))
        l.insert_pos(ele,pos)
        l.display()
    else:
        print("...please enter valid choice...")
choice()
    