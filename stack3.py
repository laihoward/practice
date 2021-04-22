
class stack_1:
    def __init__(self,stack_val=None,data=None):
        self.stack=[]
        self.stack_val =stack_val
        self.data =data
    
    def __len__(self):
        return len(self.stack)
    
    
    def isEmpty(self):
        if len(self.stack) ==0:
            return True
        else:
            return False

    def push(self,data):
        self.stack.append(data)
        print(self.stack)
        print(len(self.stack))

    def pop(self):
        top = len(self.stack)
        if  len(self.stack)==0:
            print("stack is empty")
        else:
            print("pop data is:%s" % str(self.stack[top-1]))
            top -= 1

    def peek(self):
        top = len(self.stack)
        if len(self.stack)==0:
            print("stack is empty")
        else:
            print("peek data is:%s" % str(self.stack[top-1]))
    
    def print_stack(self):
        i=1
        j=len(self.stack)
        while j >0:
            print("[%d]%s" % (i,str(self.stack[j-1])))
            j -= 1        
            i+=1

    def stack_sum(self):
        j=len(self.stack)  
        sum = 0
        stack_number =0
        if len(self.stack)==0:
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

