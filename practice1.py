import os
class Linked_Node:
    def __init__(self,point=None,name=None, next=None):
        self.name=name
        self.point=point
        self.next=next

class Linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def append(self,point,name):
        new_player = Linked_Node(point,name)
        if self.head==None:
            self.head=new_player
            self.tail=new_player
        else:
            self.tail.next=new_player
            self.tail= self.tail.next
    
    def delete_last(self):
        if self.head==None:
            print("No data")
        elif self.head.next==None:
            self.head=None
        else:
            move_node = self.head
            while move_node.next != None:
                self.tail=move_node
                move_node=move_node.next
            self.tail.next = None

    def __str__(self):
        current_node = self.head
        chain = []
        index = 1
        while current_node != None:
            chain.append("["+str(index)+"]"+str(current_node.name)+"得"+str(current_node.point)+"分")
            index += 1
            current_node = current_node.next
        return " --> ".join(chain)

def main():
    l=Linked_list()
    while True:
        
        print(" 1.加入資料 \n 2.顯示資料 \n 3.刪除最後一個資料 \n 4.結束" )
        option=input("輸入選項:")
        if option == "1":
            name=input("球員:")
            point=input("得分為:")
            l.append(point,name)
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif option == "2":
            print("="*20)
            print(l)
            print("="*20)
        
        elif option == "3":
            l.delete_last()

        elif option == "4":
            print(l)
            return False
    
if __name__ == '__main__':
    main()
