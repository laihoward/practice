import os
import linkedlist as l 
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class StackByLinkedlist():
    def __init__(self):
        # Actually, you only need to use linkedlist.py which you already created
        # to implement Stack
        self.head=Node("head")
        self.size = 0

    def isempty(self):
        return self.size == 0
    
    def push(self,data):
        # By using LinkedList defined in linkedlist.py,
        # you will not need to work with Node and manipulate its states in this script.
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next=new_node
        self.size +=1

    def pop(self):
        if  self.size == 0:
            print("stack is empty")
        else:
            pop_data = self.head.next
            print("pop data is:%s" % str(pop_data.data))
            self.size -= 1
            self.head=self.head.next    
    
    def peek(self):
        if self.size == 0:
            print("stack is empty")
        else:
            current_node = self.head
            print("peek data is:%s" % str(current_node.next.data))

    def print_Stack(self):
        current_node = self.head
        for i in range(self.size):
            print("[%d]%s" % (i+1,str(current_node.next.data)))
            current_node = current_node.next

    def stack_sum(self):
        sum = 0
        stack_number = 0
        current_node = self.head
        j=self.size
        print(j) 
        if self.size ==0:
            print("stack is empty")
        else:
            while j > 0:
                stack_number = current_node.next.data
                j  -= 1
                current_node = current_node.next
                sum = sum + stack_number         
            print("The sum of stack is:%d"% sum)


def main():
    s=StackByLinkedlist()
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("="*20)
        # print("%s筆資料" % str(top+1))
        print(" 1.加入資料 \n 2.刪除資料 \n 3.最上層資料 \n 4.顯示資料 \n 5.資料相加 \n 0.結束" )
        option=input("輸入選項:")

        if option == "0":
            return False
        elif option == "1":
            data = int(input("The data to be entered is:"))
            s.push(data)
        elif option =="2":
            s.pop()
        elif option == "3":
            s.peek()
        elif option == "4":
            s.print_Stack()
        elif option == "5":
            s.stack_sum()
            

if __name__ == '__main__':
    main()

