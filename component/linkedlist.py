import os
class Linked_Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def isempty(self):
        return self.size == 0
    
    def append(self,data):
        new_node = Linked_Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail= new_node
        self.size +=1
        
    
    def delete_last(self):
        if self.head==None:
            print("No data")
        elif self.head.next==None:
            self.head=None
            self.size -=1
        else:
            move_node = self.head
            while move_node.next != None:
                self.tail=move_node
                move_node=move_node.next
            self.tail.next = None
            self.size -=1


    def insert(self,index,data):
        if self.head==None:
            print("No data")
        if not 1 <= index <= len(self):
            print("index out of list")
        elif index == 1:
            new_node = Linked_Node(data)
            new_node.next = self.head
            self.head = new_node
        elif  1 <= index <= len(self):
            new_node = Linked_Node(data)
            index_count =1
            move_node = self.head
            while index_count+1 != index:
                move_node = move_node.next
                index_count += 1
            new_node.next = move_node.next
            move_node.next = new_node
    
    def remove(self,index):
        if self.head==None:
            print("No data")
        if index == 1 and len(self)==1:
            self.head=None
            self.tail=None
        elif index ==1 and len(self)>1:
            self.head=self.head.next

        elif 1 < index < len(self):
            index_count =1
            move_node = self.head
            while index_count != index:
                previous_node = move_node
                move_node = move_node.next
                index_count += 1
            previous_node.next = move_node.next
        
        elif index==len(self):
            index_count =1
            move_node = self.head
            while index_count != index:
                previous_node = move_node
                move_node = move_node.next
                index_count += 1
            self.tail = previous_node
            previous_node.next = None
        else:
            print("index out of range")

    def print_linkedlist(self):
        current_node = self.head
        chain = []
        for i in range(len(self)):
            print("[%d]%s" % (i+1,str(current_node.data)))
            current_node = current_node.next

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node != None:
            length += 1
            current_node = current_node.next
        return length

    def __str__(self):
        current_node = self.head
        chain = []
        index = 1
        while current_node != None:
            chain.append("["+str(index)+"]"+str(current_node.data))
            index += 1
            current_node = current_node.next
        return " --> ".join(chain)

def main():
    l=Linked_list()
    while True:
        
        print(l)
        print("?????????????????????????????????"+ str(len(l)))
        print(" 1.???????????? \n 2.???????????? \n 3.???????????????????????? \n 4.???????????? \n 5.???????????????????????? \n 6.??????" )
        option=input("????????????:")
        if option == "1":
            
            data=input("?????????:")
            l.append(data)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif option == "2":
            print("="*20)
            l.print_linkedlist()
            print("="*20)
        
        elif option == "3":
            l.delete_last()
        
        elif option == "4":
            index=int(input("????????????????????????:"))
            
            data=input("?????????:")
            l.insert(int(index),data)
            os.system('cls' if os.name == 'nt' else 'clear')        
        
        elif option == "5":
            index=int(input("????????????????????????:"))
            l.remove(int(index))
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif option == "6":
            print(l)
            return False
    
if __name__ == '__main__':
    main()
