import os
class Queue_Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class QueueByLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size = 0

    def isempty(self):
        return self.size == 0
    
    def enqueue(self,data):
        new_node = Queue_Node(data)
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail= self.tail.next
        self.size +=1

    def dequeue(self):
        if  self.size == 0:
            print("stack is empty")
        elif self.size == 1:
            self.head=None
            self.size -= 1
        else:
            pop_data = self.head
            print("pop data is:%s" % str(pop_data.data))
            self.size -= 1
            self.head=self.head.next    
    
    def peek(self):
        if self.size == 0:
            print("stack is empty")
        else:
            current_node = self.head
            print("peek data is:%s" % str(current_node.data))

    def print_queue(self):
        current_node = self.head
        for i in range(self.size):
            print("[%d]%s" % (i+1,str(current_node.data)))
            current_node = current_node.next

    def queue_sum(self):
        sum = 0
        queue_number = 0
        current_node = self.head
        j=self.size
        print(j) 
        if self.size ==0:
            print("stack is empty")
        else:
            while j > 0:
                queue_number = current_node.data
                current_node = current_node.next
                j  -= 1 
                sum = sum + queue_number         
            print("The sum of queue is:%d"% sum)

def main():
    q=QueueByLinkedlist()
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
            q.enqueue(data)
        elif option =="2":
            q.dequeue()
        elif option == "3":
            q.peek()
        elif option == "4":
            q.print_queue()
        elif option == "5":
            q.queue_sum()
            

if __name__ == '__main__':
    main()

