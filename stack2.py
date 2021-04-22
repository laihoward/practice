
class stack_1:
    def __init__(self,stack_val=10,top=-1,data=None):
        self.stack_val = stack_val
        self.stack = [None]*int(stack_val)
        self.top = top
        self.data = data


    def isEmpty():
        if self.top ==-1:
            return True
        else:
            return False

#將資料push進stack
    def push(data): 
        if self.top >= self.stack_val-1:
            print("stack_val is no space")
        else:
            self.top += 1
            self.stack[self.top]=data

    #將資料pop出stack
    def pop():
        if isEmpty():
            print("stack_val is empty")
        else:
            print("pop data is:%s" % str(stack[top]))
            top -= 1

    def print_stack():
        i=1
        while top >=0:
            print("[%d]%s" % (i,str(self.stack[top])))
            self.top -= 1        
            i+=1


def main():
    while True:
        s= stack_1()
        print(self.top)
        print(" 1.加入資料 \n 2.刪除資料 \n 3.顯示資料 \n 0.結束" )
        option=input("輸入選項:")

        if option == "0":
            return False
        elif option == "1":
            data = int(input("The data to be entered is:"))
            s.push(data)
        elif option == "2":
            s.pop()
        elif option == "3":
            s.print_stack()


if __name__ == '__main__':
    main()
