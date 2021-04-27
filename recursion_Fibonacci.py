import geometry.stack3 as s
#Compute Fibonacci number iteratively and recursively.




# class Compute_Fibonacci:
#     def __init__(self,n = None):
#         self.stack=[]
#         self.n = n
#         self.size = 0 


#     def fib(self,n):
#         s.stack_1.push(self,n)
#         num = 0
#         j = self.n
#         for i in range(j):
#             print(self.stack)
# def main():
#     C=Compute_Fibonacci()
#     n = int(input("n = "))
#     C.fib(n)



# if __name__ == '__main__':
#     main()



def fib_for(n):
    stack=[]
    num = 0
    i =0 
    for i in range(n+1):
        print(i)
        if i ==0:
            stack.append(i)
        elif i ==1:
            stack.append(i)
        else:
            num = stack[i-1]+ stack[i-2]
            stack.append(num) 
    print(stack)
    print(stack[i])
fib_for(8)


def fib_re(n): 
    if n ==0:
        return 0
    if n ==1 or n ==2:
        return 1
    if n>2:
        return fib_re(n-1)+fib_re(n-2)
    
print(fib_re(7))



# Example:
# fib(0) == 0
# fib(1) == 1
# fib(2) == 1
# fib(3) == 2
# fib(4) == 3
# fib(5) == 5
# fib(6) == 8