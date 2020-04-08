def addBinary(a, b):
    lis1 = [int(i) for i in a]
    lis2 = [int(i) for i in b]

    i = len(lis1)-1
    j = len(lis2)-1
    temp = 0
    lis = []
    while(i>=0 and j>=0):
        lis.append((lis1[i]+lis2[j]+temp)%2)
        temp = (lis1[i]+lis2[j]+temp)//2
        i-=1
        j-=1
    
    remain = lis1[0:i+1] if i>=0 else lis2[0:j+1]
    index = i if i>=0 else j
    while(index>=0):
        lis.append((remain[index]+temp)%2)
        temp = (remain[index]+temp)//2
        index-=1
    if temp == 1:
        lis.append(temp) 
    return ''.join([str(lis[i]) for i in range(len(lis)-1,-1,-1)])
   
    
print(addBinary('101','1111'))