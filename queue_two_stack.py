
import geometry.stack3 as s


class Queue_Two_Stacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0
        self.size2 = 0
        

    def enqueue(self, data):
        self.stack1.append(data)
        self.size +=1
        print(self.size)
        print("stack1 data is:%s"%str(self.stack1))

    def dequeue(self):
        if self.size2 == 0:
            if self.size == 0:
                raise IndexError("Can't dequeue from empty queue!")
            while self.size > 0:
                self.stack=self.stack1
                last_stack_1_item = s.stack_1.pop(self)
                print(last_stack_1_item)
                self.stack2.append(last_stack_1_item)
                print("stack2 data is:%s"%str(self.stack2))
                self.size2 +=1
                # print(self.size2)
        popnumber=self.stack2[self.size2-1]
        del self.stack2[self.size2-1]
        self.size2-=1
        print("pop data is:%s" % str(popnumber))
        return popnumber
    
    def print_queue(self):
        print("stack2 data is:%s"%str(self.stack2))
        # i=1
        # j=self.size2
        # while j >0:
        #     print("[%d]%s" % (i,str(self.stack[j-1])))
        #     j -= 1        
        #     i+=1



def main():
    Q=Queue_Two_Stacks()
    while True:
        # print("%s筆資料" % str(top+1))
        print("="*20)
        print(" 1.加入資料 \n 2.刪除資料 \n 3.最上層資料 \n 4.顯示資料 \n 0.結束" )
        option=input("輸入選項:")

        if option == "0":
            return False
        elif option == "1":
            data = int(input("The data to be entered is:"))
            Q.enqueue(data)
        elif option =="2":
            Q.dequeue()
        elif option == "3":
            s.peek()
        elif option == "4":
            Q.print_queue()

if __name__ == '__main__':
    main()

