class QueueByList:
    def __init__(self,data=None,top = 0):
        self.top =top
        self.queue=[]
        self.data =data
    
    def __len__(self):
        return len(self.queue)
    
    
    def isEmpty(self):
        if len(self.queue) ==0:
            return True
        else:
            return False

    def enqueue(self,data):
        self.queue.append(data)
        print(self.queue)
        print(len(self.queue))

    def dequeue(self):
        if  len(self.queue) ==0:
            print("queue is empty")
        else:
            print("pop data is:%s" % str(self.queue[self.top]))
            self.queue[self.top]=None
            self.top += 1
        
    def peek(self):
        if len(self.queue) ==0:
            print("queue is empty")
        else:
            print("peek data is:%s" % str(self.queue[self.top]))
    
    def print_queue(self):
        i=self.top
        count = 1
        j=len(self.queue)-i
        while j >0:
            print("[%d]%s" % (count,str(self.queue[i])))
            j -= 1       
            count +=1
            i+=1

    def queue_sum(self):
        i=self.top
        j=len(self.queue)-i  
        sum = 0
        queue_number =0
        if len(self.queue) ==0:
            print("queue is empty")
        else:
            while j >0:
                queue_number = self.queue[i]
                j -= 1
                i+=1
                sum = sum + queue_number         
            print("The sum of queue is:%d"% sum)



def main():
    q=QueueByList()
    while True:
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

