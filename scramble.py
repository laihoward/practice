queue = [1,2,3]

def scramble(data):
    size = len(data)
    new=[]
    count = 0
    i = 0
    a = 1
    while i < size:
        if i % 2 ==0:
            for a in range(count):
                new.append(data[i])
                print("a%d"%data[i])
                i+=1
        elif i % 2 ==1:
            j = 0
            while count>=j:
                new.append(data[count-j+i])
                print("b%d" % new[i+j])
                j=j+1
            count+=2
            i=i+count
    print(new)
        

scramble(queue)