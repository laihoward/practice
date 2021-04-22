stack_val = 10
global stack
stack = [None]*stack_val
top = -1

def isEmpty():
    if top ==-1:
        return True
    else:
        return False

#將資料push進stack
def push(data):
    global stack
    global stack_val
    global top
    if top >= stack_val-1:
        print("stack_val is no space")
    else:
        top += 1
        stack[top]=data

#將資料pop出stack
def pop():
    global stack
    global top
    if isEmpty():
        print("stack is empty")
    else:
        print("pop data is:%d" % stack[top])
        top -= 1

def peek():
    global top
    global stack
    if isEmpty():
        print("stack is empty")
    else:
        print("peek data is:%d" % stack[top])


def print_stack():
    global top
    global stack
    i=1
    j=top
    while j >=0:
        print("[%d]%d" % (i,stack[j]))
        j -= 1        
        i+=1




def main():
    while True:
        print("%s筆資料" % str(top+1))
        print(" 1.加入資料 \n 2.刪除資料 \n 3.顯示資料 \n 4.最上層資料 \n 0.結束" )
        option=input("輸入選項:")

        if option == "0":
            return False
        elif option == "1":
            data = int(input("The data to be entered is:"))
            push(data)
        elif option == "2":
            pop()
        elif option == "3":
            print_stack()
        elif option == "4":
            peek()


if __name__ == '__main__':
    main()
