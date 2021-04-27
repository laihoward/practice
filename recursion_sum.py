#Given a non-negative int n, return the sum of its digits recursively.



def sumDigits(num):
    x=0
    global sum
    if num < 0:
        print("input another number")
    elif num > 0:
        x = num % 10
        sum = sum + x
        num = (num-x)/10
        sumDigits(num)
    else:
        print(sum)
        sum = 0


def main():
    global sum
    sum = 0
    sumDigits(12) 
    sumDigits(126) 
    sumDigits(49) == 13


if __name__ == '__main__':
    main()


