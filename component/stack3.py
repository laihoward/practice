class stack_1:
    def __init__(self,stack_val=None,data=None):
        self.stack=[]
        self.stack_val =stack_val
        self.data =data
        self.size = 0
    
    def __len__(self):
        return self.size
    
    
    def isEmpty(self):
        if self.size ==0:
            return True
        else:
            return False

    def push(self,data):
        self.stack.append(data)
        print(self.stack)
        print(self.size)
        self.size +=1

    def pop(self):
        if  self.size==0:
            print("stack is empty")
        else:
            # print("pop data is:%s" % str(self.stack[self.size-1]))
            deldata = self.stack[self.size-1]
            del self.stack[self.size-1]
            self.size -=1
            return deldata

    def peek(self):
        
        if self.size==0:
            print("stack is empty")
        else:
            print("peek data is:%s" % str(self.stack[self.size-1]))
    
    def print_stack(self):
        i=1
        j=self.size
        while j >0:
            print("[%d]%s" % (i,str(self.stack[j-1])))
            j -= 1        
            i+=1

    def stack_sum(self):
        j=self.size
        sum = 0
        stack_number =0
        if self.size==0:
            print("stack is empty")
        else:
            while j >0:
                stack_number = self.stack[j-1]
                j -= 1
                sum = sum + stack_number         
            print("The sum of stack is:%d"% sum)



def main():
    s=stack_1()
    while True:
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
            s.print_stack()
        elif option == "5":
            s.stack_sum()
            

if __name__ == '__main__':
    main()

